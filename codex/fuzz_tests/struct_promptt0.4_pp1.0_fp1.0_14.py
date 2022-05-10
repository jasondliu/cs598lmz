import _struct
# Test _struct.Struct

# _struct.Struct(fmt)
# fmt is a string, like 'hhl'
# Return a new Struct object which writes and reads binary data according to the format string fmt

# struct.pack(fmt, v1, v2, ...)
# fmt is a string, like 'hhl'
# Return a string containing the values v1, v2, ... packed according to the given format.

# struct.unpack(fmt, string)
# fmt is a string, like 'hhl'
# Return a tuple containing the values unpacked according to the given format.
# The string must contain exactly the amount of data required by the format (len(string) must equal struct.calcsize(fmt)).

# struct.calcsize(fmt)
# Return the size of the struct (and hence of the string) corresponding to the given format.

# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# Pack the values v1, v2, ... according to the given format. The result is written to the writable buffer buf starting at position offset.
