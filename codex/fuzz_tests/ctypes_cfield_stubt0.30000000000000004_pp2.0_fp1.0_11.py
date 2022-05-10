import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert repr(S.x) == "<CField 'x' of 'S' objects>"

def test_cfield_from_address():
    s = S()
    assert repr(ctypes.CField.from_address(ctypes.addressof(s), S, 'x')) == "<CField 'x' of 'S' objects>"

def test_cfield_from_address_with_offset():
    s = S()
    assert repr(ctypes.CField.from_address(ctypes.addressof(s), S, 'x', 1)) == "<CField 'x' of 'S' objects>"

def test_cfield_from_address_with_offset_and_size():
    s = S()
    assert repr(ctypes.CField.from_address(ctypes.addressof(s), S, 'x', 1, ctypes.sizeof(ctypes.c_int))) == "<CField 'x' of 'S' objects>"

def test_cfield_from_address_with_offset
