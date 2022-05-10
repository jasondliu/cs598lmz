import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    __slots__ = ['x', 'y']
