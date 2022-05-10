import ctypes
import ctypes.util
import threading
import sqlite3


class glib2:
    class GError(ctypes.Structure):
        _fields_ = [
            ('domain', ctypes.c_int),
            ('code', ctypes.c_int),
            ('message', ctypes.c_char_p)
        ]

    class GVariant(ctypes.Structure):
        _fields_ = [
            ('type', ctypes.c_int)
        ]

    _GLIB2_LIB_NH = ctypes.util.find_library('libgobject-2.0-0')

    if _GLIB2_LIB_NH is None:
        _GLIB2_LIB_NH = ctypes.util.find_library('libgobject-2.0')

    _GLIB2_LIB = ctypes.CDLL(_GLIB2_LIB_NH)
    _GLIB2_LIB.g_variant_get_type_string.restype = ctypes.c_char_p
