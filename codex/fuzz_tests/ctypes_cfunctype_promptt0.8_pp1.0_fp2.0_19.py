import ctypes
# Test ctypes.CFUNCTYPE(None)
with assert_raises(TypeError) as ex:
    ctypes.CFUNCTYPE(None)(lambda: None)
assert str(ex.value) == 'CFUNCTYPE() arg 1 must be a callable'
with assert_raises(TypeError) as ex:
    ctypes.CFUNCTYPE(None, [])(lambda: None)
assert str(ex.value) == 'CFUNCTYPE() arg 1 must be a callable'
with assert_raises(TypeError) as ex:
    ctypes.CFUNCTYPE(None, None)(lambda: None)
assert str(ex.value) == 'CFUNCTYPE() arg 1 must be a callable'
with assert_raises(TypeError) as ex:
    ctypes.CFUNCTYPE(None, None, None)(lambda: None)
assert str(ex.value) == 'CFUNCTYPE() arg 1 must be a callable'
with assert_raises(TypeError) as ex:
    ctypes.CFUNCTYPE(None, None,
