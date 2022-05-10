import weakref
# Test weakref.ref on a class which uses slots, argtypes, restype and
# errcheck.
from ctypes import *
from ctypes.test import cdll

class X(Structure):
    _fields_ = [("x", c_int)]
    _argtypes_ = [POINTER(X)]
    _restype_ = c_int

    def __init__(self):
        self.value = cdll.test_func.__dict__["test17_struct"](self)

    def __del__(self):
        self.value = cdll.test_func.__dict__["test17_struct"](self)

x = X()

def callback(object):
    pass

ref = weakref.ref(x, callback)

del x
