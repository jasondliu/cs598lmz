import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_from_address():
    s = S()
    assert ctypes.CField.from_address(ctypes.addressof(s), S, 'x') is s.x

def test_cfield_from_address_exception():
    s = S()
    with raises(TypeError):
        ctypes.CField.from_address(ctypes.addressof(s), S, 'y')

def test_cfield_from_address_exception_2():
    s = S()
    with raises(TypeError):
        ctypes.CField.from_address(ctypes.addressof(s), S, 'x', S)

def test_cfield_from_address_exception_3():
    s = S()
    with raises(TypeError):
        ctypes.CField.from_address(ctypes.addressof(s), S, 'x', S, 'y')
