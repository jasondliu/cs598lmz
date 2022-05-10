import _struct
# Test _struct.Struct
def test_struct_1():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(10) == b'\n\x00\x00\x00'
    assert s.unpack(b'\n\x00\x00\x00') == (10,)

def test_struct_2():
    s = _struct.Struct('l')
    assert s.size == 8
    assert s.pack(10) == b'\n\x00\x00\x00\x00\x00\x00\x00'
    assert s.unpack(b'\n\x00\x00\x00\x00\x00\x00\x00') == (10,)

def test_struct_3():
    s = _struct.Struct('c')
    assert s.size == 1
    assert s.pack(b'x') == b'x'
    assert s.unpack(b'x') == (b'x',)

def test_struct_4():
    s = _
