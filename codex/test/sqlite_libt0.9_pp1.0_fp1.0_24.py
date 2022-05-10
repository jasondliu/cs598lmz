import ctypes
import ctypes.util
import threading
import sqlite3
from collections import defaultdict

from ..component import Component
from ..message import Message
from ..utils import separate_dict, PRunner
from ..config import config

ADD = 0
ADD_POL = 1
DEL = 2
DEL_POL = 3
ADD_LOCAL = 4
DEL_LOCAL = 5

libctl = ctypes.cdll.LoadLibrary(ctypes.util.find_library("nancat-libctl"))
libctl.handle_packet.restype = ctypes.c_int32
libctl.handle_packet.argtypes = [ctypes.c_int32, ctypes.c_int32]
libctl.filter_update.argtypes = [ctypes.c_int32]
libctl.get_rtable.restype = ctypes.c_void_p
libctl.get_rtable.argtypes = [ctypes.c_char_p]
libctl.get_filter.restype = ctypes.c_void_p
libctl.get_filter.argtypes = [ctypes.c_char_p]


