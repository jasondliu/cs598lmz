import _struct
# Test _struct.Struct creation with an unicode format string.
value = _struct.Struct(u"s")
# Check that we get the correct size for a string.
value.size
