from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack(format, v1, v2, ...)
# Return a bytes object containing the values v1, v2, ... packed according to the given format. The arguments must match the values required by the format exactly.

# _struct.Struct.unpack(bytes)
# Unpack the values contained in the bytes object according to the format string, and return a tuple containing the unpacked values.

# _struct.Struct.iter_unpack(bytes)
# Unpack the values contained in the bytes object according to the format string, and return an iterator over the unpacked values.

# _struct.Struct.calcsize(format)
# Return the size in bytes of the struct (and hence of the bytes object produced by pack(format, ...)) corresponding to the format string.

# _struct.Struct.format
# The format string used to construct this Struct object.

# _struct.Struct.size
# The size in bytes of the struct corresponding to the format string.

# _struct.Struct.unpack_from
