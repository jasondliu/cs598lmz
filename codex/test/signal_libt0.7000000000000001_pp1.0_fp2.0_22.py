import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import struct
from scapy.all import *
import time
import threading
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', default="eth0", help="Interface to send packets")
parser.add_argument('-p', '--pcap', default="", help="Input pcap file")
parser.add_argument('-d', '--display', type=int, default=0, help="0-10, 0=no display")
parser.add_argument('-v', '--video', action='store_true', default=False, help="Video")
parser.add_argument('-c', '--codec', type=str, default="", help="Codec, x264 or x265")
parser.add_argument('-r', '--rate', type=float, default=0.0, help="Rate")
