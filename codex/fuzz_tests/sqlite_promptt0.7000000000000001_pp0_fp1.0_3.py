import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("rmotr.db")
from os import path

PATH = path.dirname(path.abspath(__file__))
#db_path = "rmotr.db"
db_path = path.join(PATH, "rmotr.db")

_libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

def _check_null_char(buf, max_length):
    first_null = buf.find(b'\x00')
    if first_null != -1:
        raise ValueError("Embedded null character")
    if len(buf) > max_length:
        raise ValueError("Insufficient space")

def _check_null_terminated(buf, max_length):
    if len(buf) > max_length:
        # Buffer was not null terminated
        raise ValueError("Insufficient space")

def _void(name, argtypes, restype=ctypes.c_int, errcheck=None):
    return (name, ctypes.CFUNCTYPE(
