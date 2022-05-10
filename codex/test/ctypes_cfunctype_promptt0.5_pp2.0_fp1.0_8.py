import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

def func(*args):
    print(args)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.py_object)

# This should not crash
