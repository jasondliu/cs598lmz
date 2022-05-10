import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    # Test that we can pass a callable object to CFUNCTYPE
    # (ctypes issue #28)
    class X(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args):
            return self.func(*args)
    def func(x, y):
        return x + y
    x = X(func)
    CFUNCTYPE(c_int, c_int, c_int)(x)

# Test ctypes.POINTER(<type>)
def test_pointer():
    # Test that POINTER(<type>) is callable, and returns a ctypes instance
    p = POINTER(c_int)
    assert isinstance(p(42), p)
    assert p(42).value == 42

# Test ctypes.addressof
def test_addressof():
    # Test that addressof can be used as a function
    p = POINTER(c_int)
    assert addressof(p(42))
