import _struct
# Test _struct.Struct
def test_Struct():
    # Create a packed structure.
    s = _struct.Struct("5s 3s b c h")
    # Get a string containing the packed structure.
    packed = s.pack("abcde", "def", 65, 66, 67)
    # Create a structure from the packed string.
    unpacked = s.unpack(packed)
    # Print the results.
    print(unpacked)
    assert unpacked == ("abcde", "def", 65, 66, 67)
