import _struct
# Test _struct.Struct

def test_init():
    # test __init__()
    s = _struct.Struct('i')
    assert s.format == 'i'

    raises(TypeError, _struct.Struct, 'i', 'foo')

def test_size():
    # test size
    s = _struct.Struct('i')
    assert s.size == _struct.calcsize('i')
    s = _struct.Struct('ii')
    assert s.size == _struct.calcsize('ii')

def test_pack():
    # test pack()
    s = _struct.Struct('i')
    assert s.pack(42) == _struct.pack('i', 42)
    s = _struct.Struct('ii')
    assert s.pack(1, 2) == _struct.pack('ii', 1, 2)
    raises(TypeError, s.pack, 1)
    raises(TypeError, s.pack)

def test_pack_into():
    # test pack_into()
    s = _struct.Struct('i')
    buf = array('b
