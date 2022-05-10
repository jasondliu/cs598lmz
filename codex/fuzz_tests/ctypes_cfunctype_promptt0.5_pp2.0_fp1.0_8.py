import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

def func(*args):
    print(args)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.py_object)

# This should not crash
_ctypes_test.set_cmpfunc(CMPFUNC(func))

# This should print (42, 43)
_ctypes_test.call_cmpfunc(42, 43)
