import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(D)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(E)

import ctypes.wintypes

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.wintypes.HANDLE)]

ctypes.CArray = type(F)

import ctypes.util

ctypes.util.find_library('c')

ctypes.util.find_library('m')

ctypes.util.find_library('z')

ctypes.util.find_library('zlib')

ctypes.util.find_library('zlib1')

ctypes.util.
