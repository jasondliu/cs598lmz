import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True)

import multiprocessing
import multiprocessing.sharedctypes

import logging
import sys

# sys.setcheckinterval(1000)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_mem_size():
    if sys.platform == "win32":
        return ctypes.wintypes.MEMORYSTATUSEX()
    else:
        return ctypes.c_int()


def get_mem_info(mem_size):
    if sys.platform == "win32":
        mem_size.dwLength = ctypes.sizeof(mem_size)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem_size))
    else:
        libc = ctypes.CDLL(ctypes.util.find_library("c"))
