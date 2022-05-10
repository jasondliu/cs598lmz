import _struct
# Test _struct.Struct()
struct1 = _struct.Struct('c2shlL')
struct2 = _struct.Struct('c2shlL')
struct1 == struct2

struct1 != struct2

struct1.unpack('\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00')

struct1.pack(1, 512, 1024, 2048, 4096, 8192, 16384)

# Test _struct.Struct() with format error
try:
    _struct.Struct('c2shlLd')
except _struct.error:
    pass

# Test _struct.Struct().unpack_from()
_struct.Struct('c2shlL').unpack_from('\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00')

# Test _struct.Struct().pack_into()
