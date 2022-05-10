import _struct
# Test _struct.Struct.__new__ with a variety of non-string input
# (but not unicode input, which has its own test case.)

# Should not raise a TypeError
_struct.Struct(1)
_struct.Struct(1.1)
_struct.Struct([])
_struct.Struct((1,))
