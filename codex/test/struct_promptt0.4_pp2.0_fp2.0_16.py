import _struct
# Test _struct.Struct

def test_Struct():
    # Issue #15897: struct.Struct() should not work.
    try:
        _struct.Struct()
    except TypeError:
        pass
    else:
        self.fail("Expected TypeError")

def test_unpack_from():
    s = _struct.Struct('i')
    buf = array.array('b', [0, 0, 0, 0])
    assert s.unpack_from(buf, 0) == (0,)
    buf = array.array('b', [1, 0, 0, 0])
    assert s.unpack_from(buf, 0) == (1,)
    buf = array.array('b', [1, 2, 3, 4])
    assert s.unpack_from(buf, 0) == (67305985,)
    buf = array.array('b', [1, 2, 3, 4])
    assert s.unpack_from(buf, 1) == (33686019,)
    buf = array.array('b', [1, 2, 3, 4])
    assert s
