import ctypes
import ctypes.util
import threading
import sqlite3
import re
import time
import os
import sys

from . import utils
from . import net
from . import config

class _Lib(object):
    """
    Wrapper for libnetfilter_queue.
    """

    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library('netfilter_queue'), use_errno=True)
        self.lib.nfq_set_verdict.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p]
        self.lib.nfq_set_verdict.restype = ctypes.c_int
        self.lib.nfq_get_payload.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
        self.lib.nfq_get_payload.restype = ctypes.POINTER(ctypes.c_char)

