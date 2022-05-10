from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i', 'little')
s.unpack(b'\x04\x03\x02\x01')

# struct.Struct.__new__(format[, name])
# Return a new Struct object which writes and reads binary data according to the format string format.
# The format string is composed of zero or more directives:
# optional whitespace, an optional repetition count, an optional byte order, an optional alignment and a directive.
# The directives start with a single character from the set '@=<>!'.
#
# The optional whitespace and repetition count are discarded.
# The optional byte order, size and alignment specifications are combined with the directives for the next element in the format to determine the byte order, size and alignment for that element.
#
# The optional byte order part of the format string is one of:
#
#     @: native
