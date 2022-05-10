import ctypes
# Test ctypes.CField()
from ctypes import *

from ctypes.test import need_symbol


class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int, 16),
                ('a', ctypes.c_int, 16)]

class Y(ctypes.Structure):
    _fields_ = [('e', ctypes.c_int, 16),
                ('a', ctypes.c_int, 16)]

class C(ctypes.Structure):
    pass
try:
    C._fields_ = [('x', X),
                  ('y', Y)]
except TypeError as e:
    print(e)

print(C._fields_, C._pack_, C._align_)


class X(ctypes.Structure):
    pass
try:
    X._fields_ = [('a', ctypes.c_int, 16),
                  ('a', ctypes.c_int, 16)]
except ValueError as e:
    print(e)


class X(ctypes.Union):
    pass
try:
