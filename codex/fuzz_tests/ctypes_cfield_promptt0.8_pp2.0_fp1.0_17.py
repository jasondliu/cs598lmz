import ctypes
# Test ctypes.CField class
import _ctypes_test
import sys
print(ctypes.CField)
print(sys.modules['_ctypes_test'].__dict__.get('_testfunc_', None))

# check the type of ctypes._CFuncPtr
print(type(ctypes._CFuncPtr))
print(sys.modules[ctypes._CFuncPtr.__module__].__dict__.get('_testfunc_', None))

# check the type of ctypes.CField
print(ctypes.CField.__dict__.get('_testfunc_', None))

def function(x, y):
    return x * y

# check the type of the return value of int.from_bytes
# this is done in a try/catch because on systems with
# an older libffi the type is the one created by the
# libffi code
try:
    print(ctypes.c_int.from_buffer(b'12345').__dict__.get('_testfunc_', None))
except TypeError:
    pass

# check the type of the return
