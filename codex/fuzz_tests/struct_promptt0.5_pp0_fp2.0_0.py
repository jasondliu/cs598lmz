import _struct
# Test _struct.Struct
struct_test = _struct.Struct('i?f')
struct_test.size

# Test _struct.pack
struct_test.pack(1, False, 3.14159)

# Test _struct.unpack
struct_test.unpack(struct_test.pack(1, False, 3.14159))

# Test _struct.iter_unpack
list(struct_test.iter_unpack(struct_test.pack(1, False, 3.14159)))

# Test _struct.pack_into
buf = bytearray(struct_test.size)
struct_test.pack_into(buf, 0, 1, False, 3.14159)
buf

# Test _struct.unpack_from
struct_test.unpack_from(buf, 0)

# Test _struct.iter_unpack_from
list(struct_test.iter_unpack_from(buf, 0))

# Issue #14305: check that _struct.Struct can be subclassed
class S(_struct.Struct):
    def __new__(cls, fmt):
