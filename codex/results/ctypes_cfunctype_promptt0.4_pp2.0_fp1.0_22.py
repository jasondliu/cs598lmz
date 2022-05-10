import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    def func(a):
        return a
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
    assert cfunc(5) == 5

# Test ctypes.byref
def test_byref():
    a = ctypes.c_int(5)
    assert ctypes.byref(a).contents.value == 5

# Test ctypes.cast
def test_cast():
    a = ctypes.c_int(5)
    b = ctypes.cast(ctypes.byref(a), ctypes.POINTER(ctypes.c_int))
    assert b.contents.value == 5

# Test ctypes.pointer
def test_pointer():
    a = ctypes.c_int(5)
    b = ctypes.pointer(a)
    assert b.contents.value == 5

# Test ctypes.addressof
def test_addressof():
    a = ctypes.c_int(5)

