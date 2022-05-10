import _struct
# Test _struct.Struct
import sys
x = sys.maxsize
print(x.__class__)

struct = _struct.Struct('l')
print(struct.size)

# Test _struct.pack_into
data = bytearray(struct.size * 2)
struct.pack_into(data, 0, 1)
print(data)

# Test _struct.pack_into
# test values are outside of the range of numeric types supported natively
# by the MicroPython's port, so we expect an OverflowError
try:
    struct.pack_into(data, 0, 2**60)
except OverflowError:
    print('OverflowError')

# Test _struct.pack_into
try:
    struct.pack_into(data, 0, -2**60)
except OverflowError:
    print('OverflowError')

# Test _struct.unpack_from
print(struct.unpack_from(data, 0))

# Test _struct.unpack_from
# test values are outside of the range of numeric types supported natively
# by the MicroPython's port
