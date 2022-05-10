import _struct
# Test _struct.Struct

def test_Struct():
    # test _struct.Struct
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.format == "i"
    assert s.pack(1) == "\x01\x00\x00\x00"
    assert s.unpack("\x01\x00\x00\x00") == (1,)
    assert s.unpack_from("xxxx\x01\x00\x00\x00", 4) == (1,)
    assert s.unpack_from("xxxx\x01\x00\x00\x00", 4) == (1,)
    assert s.pack_into("xxxx", 4, 1) == None
    assert "xxxx\x01\x00\x00\x00" == "xxxx\x01\x00\x00\x00"
    assert s.calcsize() == 4

    raises(TypeError, s.pack)
    raises(TypeError, s.pack, 1, 2)
    raises(TypeError, s.unpack, 1)
   
