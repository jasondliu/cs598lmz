from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# _struct.Struct.__new__(format)
# Create a new Struct object which writes and reads binary data according to the format string format.
# The format string consists of one or more format units. Each format unit specifies a single data item to be packed or unpacked.
# The format string is passed to the constructor by name.
# The format string may contain whitespace characters which are ignored.
# The format string may also contain comments introduced by a hash character (#) which extend to the end of the physical line.
# The format string may contain any number of format units.
# The format string must be non-empty.
# The format string must start with an empty format unit or a format unit that starts with an endianness specification.
# The format string must not contain any duplicate format units.
# The format string must not contain any format units that are not supported by the current version of Python.
# The format string must not contain any format units that are ambiguous.
# The format string must not contain any format units that are invalid.
# The format string must not contain any format units that
