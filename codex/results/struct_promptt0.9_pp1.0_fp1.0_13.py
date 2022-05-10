import _struct
# Test _struct.Struct's unpacking argument check

with assertRaises(TypeError):
    Struct('x').unpack(b'\x1e')

with assertRaises(TypeError):
    Struct('x').unpack()

with assertRaises(TypeError):
    Struct('x').unpack(b'\x1e', 1)
