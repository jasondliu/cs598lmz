import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPtr = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

def test_c_int():
    s = S()
    s.x = 1
    assert s.x == 1
    s.x = 2
    assert s.x == 2
    assert repr(s.x) == 'c_int(2)'
    assert isinstance(s.x, ctypes.CField)
    assert isinstance(s.x, ctypes.CFieldPtr)
    assert isinstance(ctypes.pointer(s.x), ctypes.CFieldPtr)
    assert isinstance(ctypes.pointer(s.x), ctypes.POINTER(ctypes.c_int))
    assert ctypes.pointer(s.x)[0] == 2
    ctypes.pointer(s.x)[0] = 3
    assert ctypes.pointer(s.x)[0] == 3
    assert s.x == 3
   
