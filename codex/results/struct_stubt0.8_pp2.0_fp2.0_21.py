from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s.pack(b'123')
s.unpack(b'123')
 
# _struct.Struct.pack_into Docstring:
# pack_into(format, buffer, offset, v1, v2, ...)
# Unpack the values v1, v2, ... according to the format string format.

# The buffer's size in bytes must be at least:
#calcsize()

# Pack the values v1, v2, ... according to the format string format.

# The format argument to __init__() and pack() must be a format string
#composed of conversion specifications that describe how the values in the
#tuple are to be converted as by the pack() built-in function.

# Each conversion specification in format is replaced with the character
#represented by the corresponding value in the tuple.

# The result is always a bytes object.

# By default, the endianness of the current platform is assumed and the
#format string must start with one of the following format characters:

#    @native     
