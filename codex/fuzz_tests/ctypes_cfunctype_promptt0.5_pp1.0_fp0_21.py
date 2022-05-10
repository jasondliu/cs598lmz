import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
    raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_int, ctypes.c_int)
    raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_int)
    raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_int, ctypes.c_int)
    raises(TypeError, ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def test_CFUNCTYPE_prototype():
    # the prototype of the function is checked by the constructor
    raises(TypeError, ctypes.CFUNCTY
