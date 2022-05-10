import _struct
# Test _struct.Struct.pack_into

# TODO: add tests for big-endian formats

def test_pack_into_1():
    s = _struct.Struct('i')
    buf = array.array('c', '\0' * s.size)
    s.pack_into(buf, 0, 42)
    assert buf.tostring() == '*\0\0\0'

def test_pack_into_2():
    s = _struct.Struct('hh')
    buf = array.array('c', '\0' * s.size)
    s.pack_into(buf, 0, 1, 2)
    assert buf.tostring() == '\1\0\2\0'

def test_pack_into_3():
    s = _struct.Struct('hhh')
    buf = array.array('c', '\0' * s.size)
    s.pack_into(buf, 0, 1, 2, 3)
    assert buf.tostring() == '\1\0\2\0\3\0'

