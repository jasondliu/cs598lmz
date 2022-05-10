import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_functions():
    import ctypes
    assert isinstance(ctypes.addressof(S(1).x), ctypes.CField)
    assert isinstance(ctypes.addressof(S.x), ctypes.CField)
    assert isinstance(ctypes.byref(S(1).x), ctypes.CField)
    assert isinstance(ctypes.byref(S.x), ctypes.CField)
    assert isinstance(ctypes.cast(S(1).x, ctypes.c_void_p), ctypes.CField)
    assert isinstance(ctypes.cast(S.x, ctypes.c_void_p), ctypes.CField)
    assert isinstance(ctypes.pointer(S(1).x), ctypes.POINTER(ctypes.c_int))
    assert isinstance(ctypes.pointer(S.x), ctypes.POINTER(ctypes.c_int))
    assert isinstance(ctypes.pointer(S(1)), ctypes.POINTER(S))

    for
