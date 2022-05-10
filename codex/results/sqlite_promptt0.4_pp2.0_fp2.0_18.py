import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db")

class lib_usb(object):
    def __init__(self):
        self.lib = ctypes.CDLL(ctypes.util.find_library("usb-1.0"))
        self.ctx = ctypes.c_void_p()
        self.lib.usb_init(ctypes.byref(self.ctx))
        self.lib.usb_find_busses.restype = ctypes.c_int
        self.lib.usb_find_devices.restype = ctypes.c_int
        self.lib.usb_get_busses.restype = ctypes.POINTER(usb_bus)
        self.lib.usb_open.restype = ctypes.POINTER(usb_dev_handle)
        self.lib.usb_close.restype = ctypes.c_int
        self.lib.usb_get_string_simple.restype = ctypes.c_int
        self.lib.usb_get_string_simple.argtypes = [ctypes.POINTER(usb_dev_handle
