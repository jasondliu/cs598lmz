from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<b")
s.unpack(b"\x01")

# struct.Struct.__new__(format) -> new Struct object
# struct.Struct.__init__(format)
#
# Return a new Struct object which writes and reads binary data according to
# the format string format. The format string consists of optional whitespace,
# an optional byte order specifier, an optional fill character, an optional
# alignment specifier, and a sequence of format units. Each format unit
# specifies a single native data type. The first character of the format string
# specifies byte order, size and alignment:
#
# @: native order, size and alignment (default)
# =: native order, std. size and alignment
# <: little-endian, std. size and alignment
# >: big-endian, std. size and alignment
# !: same as >
#
# The remaining characters of the format unit (except the optional
# alignment specifier) are:
#
# x: pad byte (no data);
# c:char;
# b:signed byte; B:unsigned
