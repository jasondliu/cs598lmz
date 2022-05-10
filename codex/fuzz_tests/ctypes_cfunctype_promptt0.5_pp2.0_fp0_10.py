import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    def callback(a, b):
        return a + b
    cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(callback)
    assert cb(2, 3) == 5
    assert cb(-2, 3) == 1
    assert cb(sys.maxint, sys.maxint) == -2
    py.test.raises(OverflowError, cb, sys.maxint, sys.maxint+1)

# Test ctypes.py_object
def test_py_object():
    class X(object):
        pass
    x = X()
    y = ctypes.py_object(x)
    assert y.value is x
    assert ctypes.py_object(y).value is x
    assert ctypes.py_object(None).value is None
    assert ctypes.py_object(1).value == 1
    assert ctypes.py_object("hello").value == "hello"
    assert ctypes.
