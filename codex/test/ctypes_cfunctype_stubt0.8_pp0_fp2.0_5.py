import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_reduce():
    raises(TypeError, ctypes.cast, 0, 1)
    raises(TypeError, ctypes.cast, 1, 0)
    raises(TypeError, ctypes.cast, 1.0, 1)
    raises(TypeError, ctypes.cast, 1, 1.0)
    raises(TypeError, ctypes.cast, 1+1j, 1)
    raises(TypeError, ctypes.cast, 1, 1+1j)
    assert ctypes.cast(1, ctypes.c_char) == '\x01'
    assert ctypes.cast(1, ctypes.c_int).value == 1
    assert ctypes.cast(1, ctypes.c_void_p).value == 1
    raises(TypeError, ctypes.cast, object(), ctypes.c_int)
    assert ctypes.cast(1, type(1)) == 1
    raises(TypeError, ctypes.cast, object(), 'foo')
    assert ctypes.cast(1, 'foo') == 'foo'
   
