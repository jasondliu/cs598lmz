import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("xev.db")


Xlib = ctypes.CDLL("libX11.so.6")
X = ctypes.CDLL("libX11.so.6")


class XScreen(ctypes.Structure):
    _fields_ = [
        ('ext_data', ctypes.c_void_p),
        ('display', ctypes.c_void_p),
        ('root', ctypes.c_uint32),
        ('width', ctypes.c_int),
        ('height', ctypes.c_int),
        ('mwidth', ctypes.c_int),
        ('mheight', ctypes.c_int),
        ('ndepths', ctypes.c_int),
        ('depths', ctypes.c_void_p),
        ('root_depth', ctypes.c_int),
        ('root_visual', ctypes.c_void_p),
        ('default_gc', ctypes.c_void_p),
        ('cmap', ctypes.c_void_p),
        ('white_pixel', ctypes.c
