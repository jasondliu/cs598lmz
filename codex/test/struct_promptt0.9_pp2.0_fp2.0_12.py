import _struct
# Test _struct.Struct() and __repr__()
def test_struct():
    s = _struct.Struct("4x")
    assert repr(s).startswith("Struct(format='4x'")
    assert repr(_struct.Struct("!xHhl")).startswith("Struct(format='!xHhl")
    raises(TypeError, _struct.Struct)
    raises(TypeError, _struct.Struct, b"fghi")
    raises(TypeError, _struct.Struct, "fghi", 1, 2, 3)

    s = _struct.Struct("kKH")
    raises(TypeError, s.__repr__, 1, 2)

# Test _struct.unpack()
def test_unpack():
    s = _struct.Struct("4x")
    assert s.unpack("abcdefghi") == ((), )
    assert s.unpack("abcdefghijklmnopqrstuvwxyz")[0] == ((), )
    raises(TypeError, s.unpack)
