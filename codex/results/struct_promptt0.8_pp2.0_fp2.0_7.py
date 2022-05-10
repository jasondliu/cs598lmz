import _struct
# Test _struct.Struct
import _struct

def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4

    # test pack
    assert s.pack(0x66) == b'f\x00\x00\x00'

    # test unpack
    assert s.unpack(b"f\x00\x00\x00") == (0x66, )

    # TODO: more tests

def test_call():
    s = _struct.Struct('')
    raises(TypeError, s, ())
    raises(TypeError, s, ())
    raises(TypeError, s.__call__, ())
    raises(TypeError, s.__call__, ())

def test_unpack_from():
    s = _struct.Struct('')
    raises(TypeError, s.unpack_from, ())
    raises(TypeError, s.unpack_from, (b'',))
    raises(ValueError, s.unpack_from, (b'', 1))
