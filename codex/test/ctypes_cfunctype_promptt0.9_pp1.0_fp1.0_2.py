import ctypes
# Test ctypes.CFUNCTYPE()
def f(i, s, d):
    return i, s, d
ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_double)(f)(42, b"hello", 3.14)

# Test ctypes.byref()
def f(i, s, d):
    return ctypes.byref(i), ctypes.byref(s), ctypes.byref(d)
ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_double)(f)(42, b"hello", 3.14)

# Test ctypes argtypes
def f(i, s, d):
    return ctypes.byref(i), ctypes.byref(s), ctypes.byref(d)
ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p, ctypes.c_double)(f)
