import _struct
# Test _struct.Struct

def test_struct_i():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)

def test_struct_ii():
    s = _struct.Struct('ii')
    assert s.size == 8
    assert s.pack(42, 47) == b'*\x00\x00\x00/\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00/\x00\x00\x00') == (42, 47)

def test_struct_x():
    s = _struct.Struct('x')
    assert s.size == 1
    assert s.pack() == b''
    assert s.unpack(b'') == ()

def test_struct_3x():
    s = _struct.Struct('3x')
