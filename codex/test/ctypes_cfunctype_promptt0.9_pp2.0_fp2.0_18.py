import ctypes
# Test ctypes.CFUNCTYPE

mp_int = ctypes.c_int

def py_int_to_int(n):
    assert isinstance(n, int)
    return ctypes.c_int(n)

