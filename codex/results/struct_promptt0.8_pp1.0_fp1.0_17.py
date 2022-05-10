import _struct
# Test _struct.Struct

# _struct.Struct(fmt)

# class _struct.Struct(fmt)
#     Return a new Struct object which writes and reads binary data according to the format string fmt. 
#     See help(struct) for more on format strings.

# Format characters

# The interpretation of format strings is very similar to the interpretation of the format strings accepted by the % operator for strings. 
# For example, if you wanted to pack the tuple ('spam', 3.0, 42L) into a string, you could do it like this:

# import struct
# struct.pack('4sl', 'spam', 3.0, 42L)

#The resulting value will be a string containing 16 bytes. 
#The first four of these are just the string 'spam' represented as four bytes. 
#The next eight are the eight bytes in the IEEE 754 representation of 3.0 (the float type in Python uses the IEEE 754 representation). 
#The last four are the bytes in the big-endian (network) representation of the long integer 42. 
#You can unpack the string using the same format
