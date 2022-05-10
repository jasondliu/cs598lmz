import ctypes
# Test ctypes.CFUNCTYPE, with some generated code.
from ctypes.util import find_library
import sys

libm = ctypes.CDLL(find_library("m"))

class X:
    def __init__(self, new_value=0):
        self._value = new_value

    def set(self, new_value):
        self._value = new_value

    def get(self):
        return self._value

libm.cos.argtypes = [ctypes.c_double]
libm.cos.restype = ctypes.c_double

