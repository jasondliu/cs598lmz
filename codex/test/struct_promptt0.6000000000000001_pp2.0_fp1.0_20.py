import _struct
# Test _struct.Struct.
#
# This tests the following functions:
#     unpack
#     pack
#     calcsize
#     pack_into
#     unpack_from
#     iter_unpack
#
# The pack_into/unpack_from functions are tested in test_array.

# The following uses the standard 'struct' module to create test data.

import struct

struct_format = 'hhl5s8sl'
struct_size = struct.calcsize(struct_format)
struct_unpack = struct.Struct(struct_format).unpack
struct_pack = struct.Struct(struct_format).pack

def create_struct_data():
    return struct_unpack(struct_pack(
        1, -2, 3, b'four', 5, b'\x06\x07\x08\x09\x0a\x0b\x0c\x0d',
        9876543210))

