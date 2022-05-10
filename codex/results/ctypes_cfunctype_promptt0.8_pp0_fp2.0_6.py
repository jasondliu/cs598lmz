import ctypes
# Test ctypes.CFUNCTYPE with ellipsis ('...', or 'args')
SIGNATURE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_char))
def func(s):
    return s[0]
F = SIGNATURE(func)
assert F(b"h") == b"h"[0]
F = SIGNATURE(lambda x: x[0])
assert F(b"h") == b"h"[0]

# Test ctypes.CFUNCTYPE with (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
def func(s, n):
    return s[n]
F = SIGNATURE(func, (ctypes.POINTER(ctypes.c_char), ctypes.c_int))
assert F(b"hello", 3) == b"hello"[3]
F = SIGNATURE(lambda x, y: x[y], (ctypes.POINTER(ctypes.c_char), ctypes.c_int))
assert F(b"hello", 3) == b"hello"[3
