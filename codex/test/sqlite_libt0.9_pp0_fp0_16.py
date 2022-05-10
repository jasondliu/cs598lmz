import ctypes
import ctypes.util
import threading
import sqlite3
from enum import IntEnum
import pickle
from model import Model
import struct
import collections

libhelper = ctypes.CDLL(ctypes.util.find_library('helper'))
libhelper.get_type.restype = ctypes.pole.w_char_p
libhelper.get_data.restype = ctypes.c_char_p
libhelper.get_gid.restype = ctypes.c_int
libhelper.h_init(ctypes.create_string_buffer(b'libgd<gd'), 256)
libhelper.t_init(ctypes.create_string_buffer(b'task_queue_name'), 16, 256)

