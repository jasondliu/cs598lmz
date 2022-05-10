import _struct
# Test _struct.Struct
#
# There are some differences between _struct.Struct and struct.Struct.
#
# - _struct.Struct can use ">" as its format string (see below).
# - _struct.Struct.pack() returns bytes, not a string.
# - _struct.Struct.unpack() accepts bytes, not a string.

# This test checks that _struct.Struct accepts ">" as a format string.
# This is useful for pack() and unpack() calls that need to be endian-
# independant.
s = _struct.Struct('>i')

# Packing and unpacking a struct that has a format string that starts with
# '>' should work.
s.pack(1)
s.unpack(s.pack(1))

# Packing and unpacking a struct that has a format string that starts with
# '<' should work too.
s = _struct.Struct('<i')
s.pack(1)
s.unpack(s.pack(1))

# The argument to pack() must be bytes.
try:
    s.pack(b'x')
