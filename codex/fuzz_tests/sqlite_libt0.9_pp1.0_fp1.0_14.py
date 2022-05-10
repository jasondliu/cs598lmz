import ctypes
import ctypes.util
import threading
import sqlite3

class pi_blaster_raw(object):
    class pulse(ctypes.Structure):
        _fields_ = [("gpio", ctypes.c_int), ("delay", ctypes.c_uint32), ("duration", ctypes.c_uint32)]

    def __init__(self):
        self._lib = None
        self._handle = None

    def open(self, device="/dev/pi-blaster"):
        libname = ctypes.util.find_library("pi-blaster")
        if not libname:
            raise Exception("pi-blaster library not found")
        self._lib = ctypes.CDLL(libname)

        self._lib.pi_blaster_open.restype = ctypes.c_int
        self._handle = self._lib.piblaster_open(device, ctypes.c_uint32(0))
        if self._handle < 0:
            raise Exception("pi-blaster open failed: %d" % self._handle)

    def close(self):
        if self._lib and self._handle:

