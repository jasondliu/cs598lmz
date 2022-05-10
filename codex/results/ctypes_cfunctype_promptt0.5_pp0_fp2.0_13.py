import ctypes
# Test ctypes.CFUNCTYPE
def func(x):
    return x + 1

cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
print(cfunc(2))
# Test ctypes.POINTER
cfunc = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))(func)
print(cfunc(2))
# Test ctypes.byref
cfunc = ctypes.byref(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func))
print(cfunc(2))
# Test ctypes.cast
cfunc = ctypes.cast(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func), ctypes.c_void_p)
print(cfunc(2))

# Test ctypes.memmove
src = b'abcdefg'
dst = b'xxxxxxx'
ctypes.memmove(dst, src, len(src))

