import ctypes
# Test ctypes.CFUNCTYPE.

# Make sure this compiles.
class obj(ctypes.Structure):
    _fields_ = [("val", ctypes.c_int)]
o = obj()
callback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(lambda x: None)
callback(ctypes.pointer(o))
callback.__name__
# Check that the wrapper's __name__ is set correctly.

def func_with_custom_name():
    pass

CFUNCTYPE(None)(func_with_custom_name)
# issue9129
from ctypes import *
import sys

mpz_t = c_void_p

c_is_zero = CFUNCTYPE(c_int, mpz_t)(("mpz_cmp_ui", windll.libc))
c_is_zero.__name__
c_is_zero.__doc__
c_is_zero(0)
# issue18080
from ctypes import *

for _ in range(100):
    CFUNCTYPE(None)(lambda
