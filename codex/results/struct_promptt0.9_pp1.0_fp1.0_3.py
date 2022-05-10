import _struct
# Test _struct.Struct
struct = _struct.Struct('hhl')
data = struct.pack(1, 2, 3)
struct.unpack(data)
# inherits from 'object'
