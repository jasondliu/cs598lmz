import _struct
# Test _struct.Struct('L', ...) issue

a = _struct.pack('L', 1)
s = _struct.Struct('L')
b = s.unpack_from(a)
print type(b), b
