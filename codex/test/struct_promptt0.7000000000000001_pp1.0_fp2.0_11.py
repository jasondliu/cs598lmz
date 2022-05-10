import _struct
# Test _struct.Struct()

TestError = _struct.error

# Create template
s = _struct.Struct('hhl')

# Create buffer

b = _struct.pack('hhl', 1, 2, 3)

m = s.unpack(b)

