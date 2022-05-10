import ctypes
import ctypes.util
import threading
import sqlite3

# load the library
lib = ctypes.CDLL(ctypes.util.find_library('pcap'))

# define some constants
PCAP_ERRBUF_SIZE = 256
PCAP_ERR = -1
PCAP_IF_LOOPBACK = 0x00000001
PCAP_OPENFLAG_PROMISCUOUS = 0x00000001
PCAP_OPENFLAG_MAX_RESPONSIVENESS = 0x00000002
PCAP_OPENFLAG_NOCAPTURE_RPCAP = 0x00000004
PCAP_OPENFLAG_NOCAPTURE_LOCAL = 0x00000008
PCAP_OPENFLAG_MONITOR = 0x00000020

# define types
pcap_t = ctypes.c_void_p
bpf_u_int32 = ctypes.c_uint
pcap_handler = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint)

# define error class
class
