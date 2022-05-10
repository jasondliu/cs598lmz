import _struct
# Test _struct.Struct.__doc__
assert _struct.Struct.__doc__ == "Compiled struct object"
# Test _struct.Struct.format
assert _struct.Struct("i").format == "i"
assert _struct.Struct("<i").format == "<i"
assert _struct.Struct(">i").format == ">i"
assert _struct.Struct("=i").format == "=i"
assert _struct.Struct("!i").format == "!i"
assert _struct.Struct("@i").format == "@i"
assert _struct.Struct("=@i").format == "=@i"
assert _struct.Struct("!@i").format == "!@i"
# Test _struct.Struct.size
assert _struct.Struct("i").size == 4
assert _struct.Struct("<i").size == 4
assert _struct.Struct(">i").size == 4
assert _struct.Struct("=i").size == 4
assert _struct.Struct("!i").size == 4
assert _struct.Struct("@i").size == 4
assert _struct.Struct("=@i").size
