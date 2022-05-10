import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import shutil

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def get_int_data(data, offset=0):
    return int.from_bytes(data[offset:offset+4], byteorder='little')

def get_short_data(data, offset=0):
    return int.from_bytes(data[offset:offset+2], byteorder='little')

def get_str_data(data, offset=0, size=1):
    return data[offset:offset+size].decode('utf-8')

def get_bool_data(data, offset=0):
    return bool(data[offset])

def get_float_data(data, offset=0):
    return struct.unpack('<f', data[offset:offset+4])[0]

def get_double_data(data, offset=0):
    return struct.unpack('<d', data[offset:offset+8])[0]

def get_int64_data(data, offset=0
