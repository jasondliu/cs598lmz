import _struct
# Test _struct.Struct

# Test that the size of a struct is computed correctly
# (this is a regression test for SF bug #819668)
assert _struct.calcsize("P") == _struct.calcsize("PP") // 2

# Test that the size of a struct containing a bit field is computed correctly
# (this is a regression test for SF bug #819668)
assert _struct.calcsize("i") * 8 == _struct.calcsize("i:7")

# Test that the size of a struct containing a bit field is computed correctly
# (this is a regression test for SF bug #819668)
assert _struct.calcsize("i") * 8 == _struct.calcsize("i:7")

# Test that the size of a struct containing a bit field is computed correctly
# (this is a regression test for SF bug #819668)
assert _struct.calcsize("i") * 8 == _struct.calcsize("i:7")

# Test that the size of a struct containing a bit field is computed correctly
# (this is a regression test for SF bug #8
