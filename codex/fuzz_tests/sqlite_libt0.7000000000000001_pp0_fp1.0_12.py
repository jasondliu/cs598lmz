import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import re
import time
import wave

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.gettimeofday.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
libc.gettimeofday.restype = ctypes.c_int

class Timeval(ctypes.Structure):
    _fields_ = [("tv_sec", ctypes.c_long), ("tv_usec", ctypes.c_long)]

class TcpFlow(object):
    def __init__(self, ip1, ip2, port1, port2, proto):
        self.ip1 = ip1
        self.ip2 = ip2
        self.port1 = port1
        self.port2 = port2
        self.proto = proto
        self.time1 = 0
        self.time2 = 0
        self.total_bytes = 0
        self.syn_bytes = 0
        self.ack_bytes = 0
        self.bytes1
