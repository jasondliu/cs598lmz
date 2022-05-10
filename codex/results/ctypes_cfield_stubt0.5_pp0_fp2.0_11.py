import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    _anonymous_ = ['a']

import sys

if sys.platform == "win32":
    ctypes.windll.kernel32.GetStdHandle.argtypes = [ctypes.c_ulong]
    ctypes.windll.kernel32.GetStdHandle.restype = ctypes.c_ulong
    ctypes.windll.kernel32.GetCurrentProcessId.restype = ctypes.c_ulong
    ctypes.windll.kernel32.Get
