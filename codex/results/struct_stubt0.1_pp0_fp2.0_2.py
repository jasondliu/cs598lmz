from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack(format, v1, v2, ...)
# Return a string containing the values v1, v2, ... packed according to the given format.
# The arguments must match the values required by the format exactly.

# _struct.Struct.unpack(fmt, string)
# Unpack the string (presumably packed by pack(fmt, ...)) according to the given format.
# The result is a tuple even if it contains exactly one item.
# The string must contain exactly the amount of data required by the format (len(string) must equal calcsize(fmt)).

# _struct.Struct.unpack_from(fmt, buffer[, offset=0])
# Unpack the buffer according to the given format.
# The result is a tuple even if it contains exactly one item.
# The buffer’s size in bytes must match the size required by the format (len(buffer[offset:]) must equal calcsize(fmt)).

# _struct.Struct.iter_unpack(f
