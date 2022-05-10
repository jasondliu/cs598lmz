import _struct
# Test _struct.Struct

def test_struct_error():
    assertRaises(TypeError, _struct.Struct, "")
    assertRaises(TypeError, _struct.Struct, "I", 1)
    assertRaises(TypeError, _struct.Struct, "I", "I")
    assertRaises(TypeError, _struct.Struct, "I", "foo", 1)
    assertRaises(TypeError, _struct.Struct, "I", "foo", "bar")
    assertRaises(TypeError, _struct.Struct, "I", "foo", "foo", 1)
    assertRaises(TypeError, _struct.Struct, "I", "foo", "foo", "bar")

def test_struct_string():
    S = _struct.Struct("")
    assertEqual(S.format, "")
    assertEqual(S.size, 0)
    assertEqual(S.alignment, 0)

    S = _struct.Struct("I")
    assertEqual(S.format, "I")
    assertEqual(S.size, 4)
    assertE
