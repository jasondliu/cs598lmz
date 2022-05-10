import ctypes
# Test ctypes.CFUNCTYPE
def f(x):
    return x

f_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f_t(f)

# Test ctypes.POINTER
def f_ptr(x):
    return x

f_ptr_t = ctypes.POINTER(f_t)
