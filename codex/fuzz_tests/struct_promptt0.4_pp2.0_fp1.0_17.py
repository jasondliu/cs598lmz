import _struct
# Test _struct.Struct

def test_Struct():
    import array
    import _struct
    s = _struct.Struct('hhl')
    a = array.array('b')
    a.fromstring('\x01\x02\x00\x00\x00\x03\x00\x04')
    assert s.unpack(a) == (258, 771, 67305985)

# Test _struct.pack

def test_pack():
    import _struct
    assert _struct.pack('hhl', 1, 2, 3) == '\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00'

# Test _struct.unpack

def test_unpack():
    import _struct
    assert _struct.unpack('hhl', '\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00') == (1, 2, 3)

# Test _struct.cal
