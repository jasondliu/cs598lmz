import _struct
# Test _struct.Struct

# The format string used for testing.
fmt = 'hhl5s'

# The expected size of the above format.
size = _struct.calcsize(fmt)

# The expected exception raised by an incorrect format.
error = TypeError

# Expected results from packing various data values.
packed = {
    'abc': b'\x61\x00\x62\x00\x63\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    'a\x00c': b'\x61\x00\x00\x00\x63\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
