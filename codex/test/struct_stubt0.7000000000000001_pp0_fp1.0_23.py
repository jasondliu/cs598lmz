from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct
# _struct.Struct.__init__
# _struct.Struct.pack
# _struct.Struct.__new__

# object.__new__(cls, *args) -> a new object with type S, a subtype of T
# Called to create a new instance of class cls.
# args must be a tuple.

# _struct.Struct.__init__(fmt, *, endian='@', align=True, unicode=False)
# Return a new Struct object which writes and reads binary data according to the format string fmt.
#
# fmt must be a str object which specifies the format. The format string consists of a sequence of format units,
# each of which is a single character or an encoding like ‘<i’, ‘>q’ or ‘@P’. The optional first character
# specifies ‘native’ or ‘standard’ size and byte ordering and alignment:
#
# ...

# _struct.Struct.pack(v1, v
