from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack(format, v1, v2, ...)
# Return a string containing the values v1, v2, ... packed according to the
# format string format. The arguments must match the values required by the
# format exactly.

# _struct.Struct.unpack(fmt, string)
# Unpack the string (presumably packed by Struct.pack(fmt, ...)) according to
# the format string fmt. The result is a tuple even if it contains exactly one
# item. The string must contain exactly the amount of data required by the
# format (len(string) must equal calcsize(fmt)).

# _struct.Struct.calcsize(format)
# Return the size of the struct (and hence of the string) corresponding to the
# given format. The format string must not contain any repeated sub-formats
# (e.g. 'ii') or repeats (e.g. 'hhh')

# _struct.Struct.__new__(fmt)
# Return a new Struct object
