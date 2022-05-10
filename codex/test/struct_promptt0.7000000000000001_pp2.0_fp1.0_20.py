import _struct
# Test _struct.Struct
#
# Create a 'Struct' instance with a format string, and use
# the 'pack' and 'unpack' methods to convert between Python
# values and binary strings.
#
# This is a proof-of-concept only, to show that it is possible
# to have a working '_struct' module.
#
# XXX The format string syntax is different from that of the
# standard 'struct' module.  Only a subset of the standard
# format characters are supported.

fmt = 'hhl'
print(fmt)

# Create a 'Struct' instance.
s = _struct.Struct(fmt)

# The 'size' attribute is the size of the resulting struct
# in bytes.
print(s.size)

# Pack a tuple into a binary string according to the format.
values = (1, 2, 3)
b = s.pack(*values)
print(b)

# Unpack a binary string according to the format.
values = s.unpack(b)
print(values)

# Create a 'Struct' instance.
s = _struct.Struct
