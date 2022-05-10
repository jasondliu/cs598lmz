import ctypes
# Test ctypes.CFUNCTYPE

try:
    ctypes.CFUNCTYPE
except AttributeError:
    print('SKIP')
    raise SystemExit

# test basic functionality
def func(*args):
    return args

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
print(f(1, 2))

# test that it can be used as a base class
class MyCFunc(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)):
    pass

f = MyCFunc(func)
print(f(1, 2))

# test that it can be used as a base class with a different restype
class MyCFunc(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)):
    _restype_ = ctypes.c_float

f = MyCFunc(func)
print(f(1, 2))

#
