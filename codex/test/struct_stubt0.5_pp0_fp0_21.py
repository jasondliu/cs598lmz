from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4
s.unpack_from(b'\x01\x00\x00\x00', 0)

# struct.Struct.unpack_from(buffer, offset=0)
# Unpack from the buffer buffer starting at position offset.
# Return a tuple containing values unpacked according to the format string.
# buffer must contain at least the amount of data required by the format
# (len(buffer[offset:]) must be at least size).

# < : little-endian
