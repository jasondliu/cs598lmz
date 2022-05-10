import ctypes
import ctypes.util
import threading
import sqlite3


class GObject(ctypes.Structure):
    _fields_ = [('g_type_instance', ctypes.c_void_p)]

class GDBusConnection(ctypes.Structure):
    _fields_ = [('g_object', GObject)]

class GDBusProxy(ctypes.Structure):
    _fields_ = [('g_object', GObject)]

class GVariant(ctypes.Structure):
    _fields_ = [('g_type_instance', ctypes.c_void_p)]

class GError(ctypes.Structure):
    _fields_ = [('domain', ctypes.c_uint32),
                ('code', ctypes.c_int),
                ('message', ctypes.c_char_p)]

def g_variant_new(signature, *args):
    g_variant_new_func = libglib.g_variant_new
    g_variant_new_func.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
