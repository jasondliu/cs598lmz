import socket
import time

from lfcmuon import log
from lfcmuon.utils.TcpAudioStreamer import TcpAudioStreamer

sdr_addr = ('127.0.0.1', 7355)
stream_port = 7354
recv_addr = ('127.0.0.1', 7353)
stream_chunk_size = CHUNK_SIZE = 1024
max_rate = 192000
min_rate = 5000
range_min = 0
range_max = 65535
sample_size = 2
num_channels = 2

def parse_arguments():
    parser = argp.ArgumentParser(
        formatter_class=argp.ArgumentDefaultsHelpFormatter)
    parser.add_argument('f_start', type=int, help="Start frequency (Hz)")
    parser.add_argument('f_stop', type=int, help="Stop frequency (Hz)")
    parser.add_argument('step', type=int, help="Step frequency (Hz)")
    parser.add_argument('-r', '--repeats', type=
