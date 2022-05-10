import _struct
# Test _struct.Struct with a non-native format
s = _struct.Struct('<I')
# This works
s.pack(1)
# This doesn't
s.pack(1, 2)
