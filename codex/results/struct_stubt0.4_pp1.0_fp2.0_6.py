from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# _struct.Struct.pack(format, v1, v2, ...)
# Return a string containing the values v1, v2, ... packed according to the given format. The arguments must match the values required by the format exactly.

# _struct.Struct.unpack(format, string)
# Unpack the string (presumably packed by pack(format, ...)) according to the given format. The result is a tuple even if it contains exactly one item. The string must contain exactly the amount of data required by the format (len(string) must equal calcsize(format)).

# _struct.Struct.iter_unpack(format, buffer)
# Return an iterator yielding tuples unpacked from the given bytes object. The buffer’s size in bytes must be a multiple of the size of the format.

# _struct.Struct.unpack_from(format, buffer[, offset])
# Unpack the buffer according to the given format. The buffer’s size in bytes, minus offset, must be at least the size required by the format.

