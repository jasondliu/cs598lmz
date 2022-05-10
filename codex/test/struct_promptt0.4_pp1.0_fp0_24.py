import _struct
# Test _struct.Struct

def test_Struct():
    import _struct
    from _struct import Struct
    s = Struct("i")
    # check that the format string is saved
    assert s.format == "i"
    # check that the size is calculated correctly
    assert s.size == _struct.calcsize("i")
    # check that a buffer is needed
    raises(TypeError, s.pack)
    # check that the buffer size is checked
    raises(ValueError, s.pack, 0, "")
    # check that the format string is checked
    raises(TypeError, Struct, 42)
    raises(TypeError, Struct, [])
    raises(TypeError, Struct, ())
    raises(TypeError, Struct, {})
    raises(TypeError, Struct, "")
    raises(TypeError, Struct, "i", "")
    raises(TypeError, Struct, "i", "i")
    # check that the format string is parsed
    raises(ValueError, Struct, "z")
    # check that the native format string is parsed
    raises(ValueError, Struct, "=")
