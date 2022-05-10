import ctypes
import ctypes.util
import threading
import sqlite3

# TODO
# - add error handling

class GpsdError(Exception):
    def __init__(self, message):
        self.message = message

class Gpsd:
    def __init__(self, host='127.0.0.1', port=2947):
        self.gpsd = ctypes.CDLL(ctypes.util.find_library('gps'))
        self.gpsd.gps_open.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p]
        self.gpsd.gps_open.restype = ctypes.c_void_p
        self.gpsd.gps_close.argtypes = [ctypes.c_void_p]
        self.gpsd.gps_close.restype = None
        self.gpsd.gps_stream.argtypes = [ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p]
        self.g
