import ctypes
# Test ctypes.CField and ctypes.Field types
#
# CField, Field are the base classes of other types
#
# The Field type is supposed to be API-compatible with the
# ctypes.member function.

import unittest
from test import support

def field_type(ftype, offset, name, ctype):
    return type(name, (ctypes.CField, ),
                    {"offset": offset,
                     "type": ftype,
                     "name": name,
                     "__ctype__": ctype})

class S1(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int, 1),
                ("two", ctypes.c_int, 2),
                ("three", ctypes.c_int, 3),
                ("four", ctypes.c_int, 4)]

class S2(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int, 1),
                ("two", ctypes.c_int, 2),
                ("three", ctypes.c_int, 3),
                ("
