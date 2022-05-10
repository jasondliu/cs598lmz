import ctypes
import ctypes.util
import threading
import sqlite3
import re
import platform
import functools

_gobject = ctypes.CDLL(ctypes.util.find_library('gobject-2.0'))
_gst_api = ctypes.CDLL(ctypes.util.find_library('gst-1.0'))

_set_log_threshold = _gst_api.gst_debug_set_threshold_for_name
_set_log_threshold.argtypes = [ctypes.c_char_p, ctypes.c_uint]
_set_log_threshold.restype = None

_db = ctypes.c_char_p.in_dll(_gobject, 'pygobject_domain_db').value

G_MININT64 = -(1 << 63)
G_MAXINT64 = (1 << 63) - 1
G_MINLONG = ctypes.c_long(-2147483648).value
G_MAXLONG = ctypes.c_long(2147483647).value
G_MINFLOAT = ctypes.c_
