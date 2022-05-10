import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import struct
import subprocess

# The following is to load the library and set up the ctypes for the functions
# we need to call
libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

# The following is the definition of the struct that we need to use.
# This struct is defined in /usr/include/sys/socket.h
class sockaddr(ctypes.Structure):
    _fields_ = [("sa_len", ctypes.c_uint8),
                ("sa_family", ctypes.c_uint8),
                ("sa_data", ctypes.c_char * 14)]

# The following is the definition of the struct that we need to use.
# This struct is defined in /usr/include/sys/socket.h
class sockaddr_in(ctypes.Structure):
    _fields_ = [("sin_len", ctypes.c_uint8),
                ("sin_family", ctypes.c_uint8),
                ("sin_port", ctypes.c
