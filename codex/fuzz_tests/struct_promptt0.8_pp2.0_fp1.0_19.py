import _struct
# Test _struct.Struct.
s = _struct.Struct(">L")
assert s.size == _struct.calcsize(">L") == 4
s = _struct.Struct(">4x4x")
assert s.size == _struct.calcsize(">4x4x") == 8
print('passed all tests')
