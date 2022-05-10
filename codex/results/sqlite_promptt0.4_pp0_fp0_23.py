import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Constants

LIB_NAME = ctypes.util.find_library('pcap')
if not LIB_NAME:
    raise OSError('Cannot find libpcap')

PCAP_ERRBUF_SIZE = 256
PCAP_IF_LOOPBACK = 1

# Types

class pcap_pkthdr(ctypes.Structure):
    _fields_ = [
        ('ts', ctypes.c_ulong),
        ('caplen', ctypes.c_uint),
        ('len', ctypes.c_uint),
    ]

class pcap_addr(ctypes.Structure):
    pass

pcap_addr._fields_ = [
    ('next', ctypes.POINTER(pcap_addr)),
    ('addr', ctypes.c_void_p),
    ('netmask', ctypes.c_void_p),
    ('broadaddr', ctypes.c_void_p),
    ('dstaddr', ctypes.c_void_p),
]

class pcap
