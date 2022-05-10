import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *

from ctypes.test import is_resource_enabled

from sys import getrefcount as grc

class X(Structure):
    _fields_ = [("a", c_int), ("b", c_char_p)]
class Y(Structure):
    _fields_ = [("a", c_int), ("b", c_char_p)]

def callback(arg1, arg2):
    print(arg1, arg2)

def test_callbacks():
    if is_resource_enabled("printing"):
        libc = CDLL(ctypes.util.find_library("c"))
        # This is a function pointer type.
        func_type = CFUNCTYPE(c_int, c_int, c_char_p)
        # Test creating a callback object from a Python callable
        f = func_type(callback)
        f(1, "hello")
        f = CFUNCTYPE(c_int, X, POINTER(Y))(callback)
        x = X(42, b"
