import json

from lppinstru.discovery import Discovery, c_int, trigsrcAnalogOut1
import time, datetime
import zmq, math
import sys, traceback
import functools
import numpy as np
import pandas as pds
import peakutils
from juice_scm_gse.analysis import noise,fft
from juice_scm_gse import config as cfg
from juice_scm_gse.utils import mkdir

commands = {}


class DiscoCommand:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        commands[func.__name__] = func

    def make_cmd(self, channel, **kwargs):
        payload = {
            "CMD": self.func.__name__,
            "channel": channel,
            "args": kwargs
        }
        print(f"Build cmd with {payload}")
        return json.dumps(payload)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Disco_Driver(Discovery):
    def __init__(self, card=-1):
        super().__init__(card=card)
        self.digital_io_output_enable(0x0001)

    def turn_on(self):
        self.digital_io = 1

    def turn_off(self):
        self.digital_io = 0


@DiscoCommand
def do_psd(disco: Disco_Driver, psd_output_dir, psd_snapshots_count=10, psd_sampling_freq=[100000], **kwargs):
    mkdir(psd_output_dir)
    snapshot_asic_out = []
    sampling_freq_chx = int()
    for f in psd_sampling_freq:
        for step in range(psd_snapshots_count):
            res = disco.analog_in_read(ch1=False, ch2=True, frequency=f,
                                       samplesCount=disco.max_sampling_buffer)
            sampling_freq_chx = res[1]
            snapshot_asic_out.append(res[0][0])

        for i in range(len(snapshot_asic_out)):
            np.savetxt(psd_output_dir + f"/snapshot_psd_{f}Hz_{i}_asic_out.csv", snapshot_asic_out[i])
        freq_ch1, psd = noise.psd(snapshot_asic_out, sampling_freq_chx, window=True, removeMean=True)
        df = pds.DataFrame(data={"PSD_ASIC_OUTPUT": psd}, index=freq_ch1)
        df.to_csv(psd_output_dir + f"/psd_{f}Hz_.csv")


@DiscoCommand
def do_dynamic_tf(disco: Disco_Driver, d_tf_output_dir, d_tf_frequencies=np.logspace(0,6,num=200), **kwargs):
    mkdir(d_tf_output_dir)
    tf_g = []
    tf_phi = []
    tf_f = []
    for f in d_tf_frequencies:
        disco.analog_out_gen(frequency=f, shape='Sine', channel=0, amplitude=.1,offset=2.5)
        time.sleep(.3)
        res = disco.analog_in_read(ch1=True, ch2=True, frequency=min(f*disco.max_sampling_buffer/10.,disco.max_sampling_freq), samplesCount=disco.max_sampling_buffer, ch1range=10.)
        real_fs = res[1]
        data = pds.DataFrame(data={"input": res[0][0],
                                   "output": res[0][1]}, index=np.arange(0., disco.max_sampling_buffer/real_fs,
                                                                         1. / real_fs))
        data.to_csv(d_tf_output_dir + f"/dynamic_tf_snapshot_{f}Hz.csv")

        window = np.hanning(len(res[0][0]))
        in_spect = fft.fft(waveform=res[0][0], sampling_frequency=real_fs, window=window, remove_mean=True)
        out_spect = fft.fft(waveform=res[0][1], sampling_frequency=real_fs, window=window, remove_mean=True)
        freq = in_spect["f"]
        peaks = peakutils.indexes(in_spect["mod"], min_dist=2)
        for peak in peaks:
            f = in_spect["f"][peak]
            g = 20. * np.log10(out_spect["mod"][peak] / in_spect["mod"][peak])
            tf_phi.append(out_spect["phi"][peak] - in_spect["phi"][peak])
            tf_g.append(g)
            tf_f.append(f)
    tf = pds.DataFrame(data={"G(dB)":tf_g,"Phi(rad)":tf_phi},index=tf_f)
    tf.to_csv(d_tf_output_dir + f"/dynamic_tf.csv")

@DiscoCommand
def do_static_tf(disco: Disco_Driver, s_tf_output_dir,s_tf_amplitude=.5,s_tf_steps=100, **kwargs):
    mkdir(s_tf_output_dir)
    tf_vin = []
    tf_vout = []
    v_min = 2.5-s_tf_amplitude
    v_max = 2.5+s_tf_amplitude
    for step in np.arange(v_min, v_max, (v_max-v_min)/s_tf_steps):
        disco.analog_out_gen(shape='DC', channel=0,offset=step)
        time.sleep(.3)
        res = disco.analog_in_read(ch1=True, ch2=True, frequency=disco.max_sampling_buffer*4, samplesCount=disco.max_sampling_buffer, ch1range=10.)
        real_fs = res[1]
        data = pds.DataFrame(data={"input": res[0][0],
                                   "output": res[0][1]}, index=np.arange(0., disco.max_sampling_buffer / real_fs,
                                                                         1. / real_fs))
        data.to_csv(s_tf_output_dir + f"/static_tf_snapshot_{step}V.csv")

        tf_vin.append(np.mean(res[0][0]))
        tf_vout.append(np.mean(res[0][1]))
    tf = pds.DataFrame(data={"Vout": tf_vout}, index=tf_vin)
    tf.to_csv(s_tf_output_dir + f"/static_tf.csv")


@DiscoCommand
def turn_on_psu(disco: Disco_Driver, **kwargs):
    disco.turn_on()


@DiscoCommand
def turn_off_psu(disco: Disco_Driver, **kwargs):
    disco.turn_off()


@DiscoCommand
def do_measurements(disco, **kwargs):
    for measurement in [do_psd, do_dynamic_tf, do_static_tf]:
        print("turn ON PSU")
        turn_on_psu(disco)
        time.sleep(2.)
        print("start " + measurement.__name__)
        measurement(disco, **kwargs)
        print("turn OFF PSU")
        turn_off_psu(disco)
        time.sleep(2.)


def process_cmd(cmd_dict, discos):
    cmd = cmd_dict["CMD"]
    channel = cmd_dict["channel"]
    args = cmd_dict["args"]
    try:
        commands[cmd](discos[channel], **args)
        return "success"
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return "unknown command " + str(e)


def setup_ipc(push_port=9992, pull_port=9991):
    context = zmq.Context()
    push_sock = context.socket(zmq.PUSH)
    push_sock.connect(f"tcp://localhost:{push_port}")
    pull_sock = context.socket(zmq.PULL)
    pull_sock.connect(f"tcp://localhost:{pull_port}")
    return push_sock, pull_sock


def parse_cmd(cmd, discos):
    cmd["result"] = process_cmd(cmd, discos)
    return json.dumps(cmd)


def main():
    discos = {
        "CHX": Disco_Driver(cfg.asic_chx_disco.get()), "CHY": Disco_Driver(cfg.asic_chy_disco.get()), "CHZ": Disco_Driver(cfg.asic_chz_disco.get())
    }
    try:
        push_sock, pull_sock = setup_ipc()
        while True:
            cmd = json.loads(pull_sock.recv_json())
            push_sock.send_json(parse_cmd(cmd, discos))
    except Exception as e:
        print(str(e))
