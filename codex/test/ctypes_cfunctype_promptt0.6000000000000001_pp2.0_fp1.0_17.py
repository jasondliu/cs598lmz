import ctypes
# Test ctypes.CFUNCTYPE
def cb(a,b):
    return a+b

cb_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(cb)
assert cb_p(1, 2) == 3

# Test ctypes.byref
p = ctypes.c_int(1)
