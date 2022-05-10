import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(msg):
    print(msg)
    print(repr(ctypes.CField))
    print(repr(ctypes.CField.__name__))
    print(repr(ctypes.CField.__module__))
    print(repr(ctypes.CField.__qualname__))

test("direct")

import builtins
builtins.ctypes = ctypes

test("imported")

import sys
sys.modules['ctypes'] = ctypes

test("replaced")
