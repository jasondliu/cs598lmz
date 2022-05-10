import _struct
# Test _struct.Struct

def test_error():
    with pytest.raises(TypeError):
        _struct.Struct()

def test_get_format():
    s = _struct.Struct('i')
    assert s.format == 'i'
    with pytest.raises(AttributeError):
        s.format = 'f'

def test_get_size():
    s = _struct.Struct('i')
    assert s.size == 4
    with pytest.raises(AttributeError):
        s.size = 2

def test_pack():
    s = _struct.Struct('i')
    assert s.pack(42) == b'*\x00\x00\x00'
    with pytest.raises(_struct.error):
        s.pack(1.0)

def test_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    with pytest.raises(_struct.error):
        s.unpack(b'\x
