import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('z')
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct("z") should have raised TypeError'

def test_struct_unpack():
    s = _struct.Struct('i')
    buf = s.pack(1)
    assert s.unpack(buf) == (1,)
    assert s.unpack_from(buf) == (1,)
    assert s.unpack_from(buf, 0) == (1,)
    assert s.unpack_from(buf, 0, 1) == (1,)
    try:
        s.unpack_from(buf, 1)
    except _struct.error:
        pass
    else:
        raise TestFailed, '_struct.Struct("i").unpack_from(buf, 1) should have raised _struct.error'
    try:
        s.unpack_from(buf, 0, 2)
    except _struct.error:
        pass
    else:
        raise
