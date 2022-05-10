import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import re
import subprocess
import sys
import time

from socket import ntohl
from imp import load_source

from utility import *
from parser import *

#pcap_module = ctypes.CDLL(ctypes.util.find_library('pcap'))

class Flow(object):
    def __init__(self, parsed_packet):
        self.pascal = parsed_packet
        self.pkt_list = []
        self.sport = self.pascal.sport
        self.dport = self.pascal.dport
        self.smac = self.pascal.smac
        self.dmac = self.pascal.dmac
        self.src_ip = self.pascal.src_ip
        self.dst_ip = self.pascal.dst_ip
        self.parsed_packet = parsed_packet
        
        self.stime = 0.0
        self.etime = 0.0
        self.dtime = 0.0
        self
