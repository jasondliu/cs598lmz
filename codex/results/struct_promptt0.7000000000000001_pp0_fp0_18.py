import _struct
# Test _struct.Struct
_struct.Struct('P').format
_struct.Struct('P').size
_struct.Struct('P').pack(42)
_struct.Struct('P').pack_into(b'', 0, 42)
_struct.Struct('P').unpack(b'\x00\x00\x00\x00')
_struct.Struct('P').unpack_from(b'\x00\x00\x00\x00', 0)
_struct.Struct('P').unpack(b'\x00\x00\x00\x00')[0]
_struct.Struct('P').unpack_from(b'\x00\x00\x00\x00', 0)[0]

# Issue #18040: struct should not accept bytearray
try:
    _struct.Struct('P').pack(bytearray(b'\x00\x00\x00\x00'))
except TypeError:
    pass
else:
    assert False, 'expected TypeError'
try:
    _struct.Struct('P').unpack(bytear
