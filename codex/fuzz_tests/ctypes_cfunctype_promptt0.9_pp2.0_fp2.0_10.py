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

VAR = ctypes.c_long.in_dll(libm, "EDOM").value
assert VAR == 33

# We should really subclass c_long here to ensure that the c_long
# instance is still alive...
def set_errno(value):
    ctypes.c_long.in_dll(libm, "errno").value = value

x = X()
assert x.get() == 0

def Errcheck(result, func, args):
    if result == -1 and ctypes.
