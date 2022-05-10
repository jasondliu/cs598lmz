import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# CFUNCTYPE(None) takes no arguments, and does not return anything
# (ctypes.c_int)(0) is a way to convert to c_int before passing to
# the function.
prototype = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(X))
params =  (ctypes.c_int)(0), ctypes.pointer(X(1, 2))

# call function
_ctypes_test.set_callback(prototype(callback))
_ctypes_test.call_callback(params[0], params[1])

if value != (1, 2):
    raise RuntimeError, 'Wrong value %r' % (value,)
