import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys

# import our own modules
import file_monitor
import file_utils

# load our library
try:
    lib = ctypes.CDLL(ctypes.util.find_library('pcap'))
except:
    print 'error: unable to load libpcap'
    sys.exit(1)

# define the callback type
PCAP_HANDLE = ctypes.c_void_p
PCAP_CALLBACK = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_void_p)

# define the pcap methods
lib.pcap_open_live.restype = PCAP_HANDLE
lib.pcap_open_live.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
lib.pcap_close.argtypes = [PCAP_HANDLE]

