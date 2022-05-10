import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

def func_ptr(a, b):
    return a + b

func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func_ptr)

assert func(1, 2) == func_ptr(1, 2)

# Test ctypes.POINTER
assert ctypes.POINTER(ctypes.c_int) == ctypes.POINTER(ctypes.c_int)
assert ctypes.POINTER(ctypes.c_int) != ctypes.POINTER(ctypes.c_float)

# Test ctypes.c_char_p
assert ctypes.c_char_p(b"123") == ctypes.c_char_p(b"123")
assert ctypes.c_char_p(b"123") != ctypes.c_char_p(b"1234")

# Test ctypes.c_void_p
assert ctypes.c_void_p(123) == ctypes
