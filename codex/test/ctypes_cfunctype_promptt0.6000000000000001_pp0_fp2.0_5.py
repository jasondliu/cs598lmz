import ctypes
# Test ctypes.CFUNCTYPE

# In:
def f(x):
    return x + 1

# Out:
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(f)

# In:
f(1)

# Out:
2
# Test ctypes.cast

# In:
