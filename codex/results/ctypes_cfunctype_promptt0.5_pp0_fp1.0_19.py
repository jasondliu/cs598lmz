import ctypes
# Test ctypes.CFUNCTYPE
def cb(a, b):
    return a+b
cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb_func = cb_type(cb)
print(cb_func(2, 3))

# Test ctypes.WINFUNCTYPE
def cb(a, b):
    return a+b
cb_type = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb_func = cb_type(cb)
print(cb_func(2, 3))

# Test ctypes.PYFUNCTYPE
def cb(a, b):
    return a+b
cb_type = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cb_func = cb_type(cb)
print(cb_func(2, 3))
