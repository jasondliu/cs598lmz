import _struct
# Test _struct.Struct

_struct.Struct('i').pack(1)
_struct.Struct('i').pack(1, 2)
_struct.Struct('i').pack(1, 2, 3)
try:
    _struct.Struct('i').pack(1, 2, 3, 4)
except TypeError:
    pass

_struct.Struct('i').unpack(b'\x01\x00\x00\x00')
_struct.Struct('i').unpack(b'\x01\x00\x00\x00', 0)
_struct.Struct('i').unpack(b'\x01\x00\x00\x00', 1)
_struct.Struct('i').unpack(b'\x01\x00\x00\x00', 2)
_struct.Struct('i').unpack(b'\x01\x00\x00\x00', 3)
_struct.Struct('i').unpack(b'\x01\x00\x00\x00', 4)
