import ctypes
# Test ctypes.CFUNCTYPE

def cb(x):
    print("cb called with", x)
    return x + 1

cb_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cb_func = cb_type(cb)

print(cb_func(42))

# Test ctypes.PYFUNCTYPE

def cb2(x):
    print("cb2 called with", x)
    return x + 1

cb2_type = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)
cb2_func = cb2_type(cb2)

print(cb2_func(42))

# Test ctypes.WINFUNCTYPE

def cb3(x):
    print("cb3 called with", x)
    return x + 1

cb3_type = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)
cb3_func = cb3_type(cb3)

