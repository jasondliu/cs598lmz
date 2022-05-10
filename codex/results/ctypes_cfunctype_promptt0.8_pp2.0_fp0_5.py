import ctypes
# Test ctypes.CFUNCTYPE()
def func(x): return x + 1
pf = ctypes.CFUNCTYPE(ctypes.c_int)(func)
print pf(1)
# Test ctypes.cast()
x = ctypes.c_int(1)
print ctypes.cast(ctypes.byref(x), ctypes.POINTER(ctypes.c_int)).contents.value
# Test memmove()
src = ctypes.create_string_buffer("aaaaaaaaa")
dst = ctypes.create_string_buffer("bbbbbbbbbbbbbbbbbbbbbbbbb")
l = ctypes.memmove(dst, src, 3)
print dst.value
print ctypes.sizeof(src)
print ctypes.sizeof(dst)
# Test ctypes.sizeof()
print ctypes.sizeof(ctypes.c_int)
print ctypes.sizeof(ctypes.c_int * 3)
print ctypes.sizeof(ctypes.c_float * 5)
# Test ctypes.addressof()
array = (
