import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.POINTER(), ctypes.cast()

# ctypes.CFUNCTYPE:
# int cb(int)
@CFUNCTYPE(c_int, c_int)
def cb(i):
    print("cb({})".format(i))
    return 10*i

lib.test_callback.argtypes = [cb]
lib.test_callback.restype = c_int
r = lib.test_callback(cb)
print("result: {}".format(r))

# ctypes.POINTER:
# int cb(int)
@CFUNCTYPE(c_int, c_int)
def cb2(i):
    print("cb2({})".format(i))
    return 11*i

cbp = POINTER(cb2)
lib.test_callback.argtypes = [cbp]
lib.test_callback.restype = c_int
r = lib.test_callback(cb2)
print("result: {}".format(r))

# ctypes.cast:
# int c
