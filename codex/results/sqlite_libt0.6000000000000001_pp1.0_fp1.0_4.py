import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error

from sys import platform
if platform == "linux" or platform == "linux2":
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
    CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>
elif platform == "darwin":
    libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
    CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>
elif platform == "win32":
    libc = ctypes.CDLL(ctypes.util.find_library('msvcrt'), use_errno=True)
    CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>
else:
    raise Exception('Unsupported platform')
    
class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_nsec',
