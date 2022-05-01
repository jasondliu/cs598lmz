from ctypes import *
from ctypes.util import find_library

libm = CDLL(find_library('m'))

class Base(Structure):
    _fields_ = [('y', c_double),
                ('x', c_double)]

class Mid(Base):
    pass

Mid._fields_ = []

class Vector(Mid): pass

libm.atan2.argtypes = [Vector]
libm.atan2.restype = c_double

arg = Vector(y=0.0, x=-1.0)
ret = libm.atan2(arg)
print("%r" % ret)
