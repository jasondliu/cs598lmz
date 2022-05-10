import _struct
# Test _struct.Struct
def test_struct():
    # test string
    s = _struct.Struct('i')
    assert s.unpack('\x01\x00\x00\x00') == (1,)
    assert s.unpack('\x01\x00\x00\x00') == (1,)
    assert s.unpack('\xff\xff\xff\xff') == (-1,)
    assert s.unpack('\x01\x00\x00\x00') == (1,)
    assert s.unpack('\xff\xff\xff\xff') == (-1,)
    # test buffer
    import array
    a = array.array('c', '\x01\x00\x00\x00')
    assert s.unpack_from(a, 0) == (1,)
    assert s.unpack_from(a, 0) == (1,)
    a = array.array('c', '\xff\xff\xff\xff')
    assert s.unpack_from(a, 0) == (-1,)
