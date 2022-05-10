import ctypes
# Test ctypes.CFUNCTYPE
def py_func(x):
    return x + 1

c_func = ctypes.CFUNCTYPE(ctypes.c_int)(py_func)
assert c_func(2) == 3

# Test ctypes.cast
c_int = ctypes.c_int
c_float = ctypes.c_float
c_int_p = ctypes.POINTER(ctypes.c_int)

assert ctypes.cast(c_int(42), c_int_p).contents.value == 42
assert ctypes.cast(c_float(3.14), c_int_p).contents.value == 3

# Test ctypes.POINTER
assert ctypes.POINTER(ctypes.c_int)().contents is None

# Test ctypes.c_char_p
assert ctypes.c_char_p(b"abc").value == b"abc"

# Test ctypes.c_wchar_p
assert ctypes.c_wchar_p("abc").value == "abc"

# Test ctypes.c
