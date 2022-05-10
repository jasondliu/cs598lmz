import _struct
# Test _struct.Struct at module level.
self = _struct.Struct('i')
x = range(5)
y = self.pack(*x)
z = self.unpack(y)
