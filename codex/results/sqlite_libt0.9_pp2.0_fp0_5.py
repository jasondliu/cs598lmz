import ctypes
import ctypes.util
import threading
import sqlite3
import os

################################################################################

import my_udp
import bgp_core
import bgp_message

native_socket = ctypes.CDLL(ctypes.util.find_library("c"))
native_socket.socket.argtypes = [ctypes.c_int]
native_socket.socket.restype = ctypes.c_int

def socket(domain, socktype, proto):
    # fix 64 bit Mac OS X and python 2.6
    if sys.platform == "darwin":
        sock = native_socket.socket(domain, socktype, proto)
    else:
        sock = socket_orig(domain, socktype, proto)
    # TODO: fix 32 bit
    sock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
    return sock

socket_orig = socket.socket
socket.socket = socket

################################################################################

ANNOUNCE_TIMER_INTERVAL = 60
ANNOUNCE_TIMEOUT = 0.05
ANNOUNCE_RETRY = 3

DELAY_T
