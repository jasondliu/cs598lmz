import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # This is a bit tricky, because the function has to return
    # something that is callable.  A function is not callable (it's
    # a method), but a CFUNCTYPE(c_int) instance is.
    def f(n):
        return ctypes.CFUNCTYPE(c_int)(n)
    assert f(42)() == 42

# Test ctypes.byref
def test_byref():
    x = c_int()
    assert byref(x).value == 0
    x.value = 42
    assert byref(x).value == 42

# Test ctypes.addressof
def test_addressof():
    x = c_int()
    # the address of a ctypes variable is the same as the address of the
    # internal storage
    assert addressof(x) == addressof(x._objects)

# Test ctypes.string_at
def test_string_at():
    buf = create_string_buffer(b"hello world")
    data
