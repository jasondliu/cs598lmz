import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import time
import sys
import os

import common


# lib
libmp3lame = ctypes.CDLL(ctypes.util.find_library('mp3lame'))
libmp3lame.lame_encode_buffer_ieee_float.argtypes = [ctypes.c_void_p,
                                                     ctypes.c_void_p,
                                                     ctypes.c_void_p,
                                                     ctypes.c_int,
                                                     ctypes.c_void_p,
                                                     ctypes.c_int,
                                                     ctypes.c_int]
libmp3lame.lame_encode_buffer_ieee_float.restype = ctypes.c_int
libmp3lame.lame_close.argtypes = [ctypes.c_void_p]
libmp3lame.lame_close.restype = ctypes.c_int
libmp3lame.lame_init.restype = ctypes.c_void_p
libmp
