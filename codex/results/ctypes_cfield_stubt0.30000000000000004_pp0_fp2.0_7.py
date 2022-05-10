import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_repr():
    assert repr(S.x) == "<CField 'x' of 'S' objects>"

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_ctype():
    assert S.x.ctype == ctypes.c_int

def test_cfield_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_cfield_from_address():
    s = S()
    assert S.x.from_address(ctypes.addressof(s)).value == 0

def test_cfield_from_address_readonly():
    s = S()
    f = S.x.from_address(ctypes.addressof(s))
    with pytest.raises(AttributeError):
        f.value = 42

def test_cfield_from_address_writeable():
    s = S()
    f = S.x.from_address(ctypes.addressof
