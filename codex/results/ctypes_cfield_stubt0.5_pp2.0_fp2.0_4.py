import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field_attributes():
    f = S.x
    assert f.name == 'x'
    assert f.offset == 0
    assert f.index == 0
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.ctype is ctypes.c_int
    assert f.type is int
    assert f.pformat(f) == 'x'
    assert f.format == 'i'
    assert f.pack == struct.pack
    assert f.unpack == struct.unpack
    assert f.getfield(S(0)) == 0
    assert f.getfield(S(42)) == 42
    assert f.from_address(ctypes.addressof(S(0))) == 0
    assert f.from_address(ctypes.addressof(S(42))) == 42
    assert f.from_buffer(ctypes.create_string_buffer(ctypes.sizeof(S))) == 0
    assert f.from_buffer(ctypes.create_string_buffer(ctypes.size
