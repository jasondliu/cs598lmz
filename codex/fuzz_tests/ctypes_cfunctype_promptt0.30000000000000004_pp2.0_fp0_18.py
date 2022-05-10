import ctypes
# Test ctypes.CFUNCTYPE
def py_func(a, b):
    return a + b

c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_func)
print(c_func(1, 2))

# Test ctypes.POINTER
c_array = (ctypes.c_int * 3)(1, 2, 3)
print(c_array[0])

# Test ctypes.c_int.in_dll
from ctypes import CDLL
libc = CDLL("libc.so.6")
print(ctypes.c_int.in_dll(libc, "errno"))

# Test ctypes.string_at
c_array = (ctypes.c_char * 3)(b"a", b"b", b"c")
print(ctypes.string_at(c_array, 3))

# Test ctypes.cast
c_array = (ctypes.c_char * 3)(b"a", b"b", b"c")
print(ctypes
