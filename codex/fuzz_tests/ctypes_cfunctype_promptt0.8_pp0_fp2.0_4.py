import ctypes
# Test ctypes.CFUNCTYPE(None)
try:
    TestError
except NameError:
    TestError = AssertionError

try:
    ctypes.CFUNCTYPE(None)
except AttributeError:
    may_raise(AttributeError)
else:
    assert_raises(TypeError, ctypes.CFUNCTYPE, None)
    assert_raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_ubyte, ())
    assert_raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_ubyte, 1)
    assert_raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_ubyte, [])
    assert_raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_ubyte, [1, 2])
    assert_raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_ubyte, (1, 2))
    assert_raises(TypeError, ctypes.CFUNCTYPE, c
