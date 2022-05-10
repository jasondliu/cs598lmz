from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.pack(1)

# _struct.Struct.pack(format, v1, v2, ...)
# Return a bytes object containing the values v1, v2, ... packed according to the format string format.
# The arguments must match the values required by the format exactly.

# _struct.Struct.unpack(bytes)
# Unpack the bytes (presumably packed by pack(format, ...)) according to the format string. The result is a tuple even if it contains exactly one item.
# The bytes argument must contain exactly the amount of data required by the format (len(bytes) must equal calcsize(format)).

# _struct.Struct.unpack_from(bytes, offset=0)
# Unpack the buffer, containing bytes, according to the format string. The result is a tuple even if it contains exactly one item.
# The buffer’s size in bytes must match the size required by the format (len(bytes) must equal or exceed calcsize(format) + offset).

# _struct.Struct.iter_unpack(buffer)
# Un
