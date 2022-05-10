import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
from sqlite3.test.hooks import install_call_tracing, check_parameters

install_call_tracing(sqlite3, check_parameters)

def to_bytes(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s

def from_bytes(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    return s

def to_int(x):
    if isinstance(x, bool):
        return int(x)
    return x

def from_int(x):
    if isinstance(x, int):
        return bool(x)
    return x

def to_buffer_type(x):
    if isinstance(x, bytes):
        return bytearray(x)
    return x

def from_buffer_type(x):
    if isinstance(x, bytearray):
        return bytes(x)
    return x

def to_list(x):
    if is
