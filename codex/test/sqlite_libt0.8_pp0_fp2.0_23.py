import ctypes
import ctypes.util
import threading
import sqlite3
import time
import socket

libnfnetlink = ctypes.CDLL(ctypes.util.find_library('nfnetlink'))
libnetfilter_conntrack = ctypes.CDLL(ctypes.util.find_library('netfilter_conntrack'))

NFNL_SUBSYS_CTNETLINK = 1
IPPROTO_TCP = 6
TCP_CONNTRACK_ESTABLISHED = 4

class Nfgenmsg(ctypes.Structure):
    _fields_ = [
        ('nfgen_family', ctypes.c_ubyte),
        ('version', ctypes.c_ubyte),
        ('res_id', ctypes.c_ushort)
    ]

class Nfctmsg(ctypes.Structure):
    _fields_ = [
        ('cmn', Nfgenmsg),
        ('ct_family', ctypes.c_ubyte),
        ('ct_protonum', ctypes.c_ubyte),
    ]

