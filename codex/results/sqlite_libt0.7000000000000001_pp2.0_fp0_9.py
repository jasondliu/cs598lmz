import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import datetime
import time

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

_socket = libc.socket
_socket.restype = ctypes.c_int
_socket.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

_htons = libc.htons
_htons.restype = ctypes.c_ushort
_htons.argtypes = [ctypes.c_ushort]

_bind = libc.bind
_bind.restype = ctypes.c_int
_bind.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint]

_listen = libc.listen
_listen.restype = ctypes.c_int
_listen.argtypes = [ctypes.c_int, ctypes.c_uint]

_accept = libc.accept
_accept
