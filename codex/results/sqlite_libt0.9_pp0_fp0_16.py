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

class Type(IntEnum):
    None = 0
    Gd = 1
    Task = 2

class NetWorker(threading.Thread):
    def __init__(self, task_queue, model_queue, db_queue, param_queue, buffer_max_size=8192):
        super(NetWorker, self).__init__()
        self.db
