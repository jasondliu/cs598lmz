import socket
import random
import struct
import sys
import os
import time
import re
import threading
import signal
import binascii
import json

from scapy.all import *

from common import config

class PcapFile:
    def __init__(self, filename):
        self.filename = filename
        self.pkt_list = rdpcap(filename)

    def __len__(self):
        return len(self.pkt_list)

    def __getitem__(self, index):
        return self.pkt_list[index]

class PcapGenerator:
    def __init__(self, pkt_list):
        self.pkt_list = pkt_list
        self.index = 0
        self.pkt_count = len(pkt_list)

    def __len__(self):
        return self.pkt_count

    def __getitem__(self, index):
        return self.pkt_list[index]

    def __iter__(self):
        return self

    def __next__(self
