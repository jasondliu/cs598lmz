from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', False)
s.unpack(b'abcd')

# TypeError: expected bytes, not bytearray
s.unpack(bytearray(b'abcd'))

# ValueError: unpack requires a bytes object of length 8
s.unpack(b'a')

# ValueError: unpack requires a bytes object of length 8
s.unpack(b'a' * 8)

# ValueError: unpack requires a buffer of length 8
s.unpack(b'a' * 10)
# Cleanup.
del Struct

# Test code for _struct.Struct.
import _struct as struct

# Check that the repr() of a Struct object doesn't contain the
# internal format string.
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'q', 'Q', 'f', 'd', 's', 'p']:
    s = struct.Struct(fmt)
    assert fmt not in repr(s)

# Check that the format string is accepted as the
