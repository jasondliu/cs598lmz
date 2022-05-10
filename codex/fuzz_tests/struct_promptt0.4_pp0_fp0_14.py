import _struct
# Test _struct.Struct

# The following test cases are taken from the Python 2.5.2
# documentation.

# Create a buffer of 20 bytes
buf = _struct.buffer_info(b"12345678901234567890")[0]

# Create a struct object
TestStruct = _struct.Struct(b'hi')

# Test pack
packed = TestStruct.pack(1, 2)
assert packed == b'\x00\x01\x00\x02'

# Test pack_into
TestStruct.pack_into(buf, 0, 1, 2)
assert _struct.unpack_from(b'hi', buf, 0) == (1, 2)

# Test unpack
assert TestStruct.unpack(packed) == (1, 2)

# Test unpack_from
assert TestStruct.unpack_from(buf, 0) == (1, 2)

# Test iter_unpack
assert list(TestStruct.iter_unpack(packed)) == [(1, 2)]

# Test size
assert TestStruct.size == 4

# Test format
assert
