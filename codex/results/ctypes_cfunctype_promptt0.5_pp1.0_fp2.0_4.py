import ctypes
# Test ctypes.CFUNCTYPE
def func(a):
    return a

CFUNCTYPE_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
assert CFUNCTYPE_func(1) == 1

# Test ctypes.POINTER
POINTER_func = ctypes.POINTER(CFUNCTYPE_func)
assert POINTER_func[0](2) == 2

# Test ctypes.byref
assert ctypes.byref(CFUNCTYPE_func)(3) == 3

# Test ctypes.pointer
assert ctypes.pointer(CFUNCTYPE_func)[0](4) == 4

# Test ctypes.string_at
assert ctypes.string_at(CFUNCTYPE_func, 0) == b''

# Test ctypes.wstring_at
assert ctypes.wstring_at(CFUNCTYPE_func, 0) == ''

# Test ctypes.string_at_addr
assert ctypes.string_at_addr(CFUNCTYPE_func,
