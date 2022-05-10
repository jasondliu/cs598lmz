from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = 8
s.pack(1, 2, 3)

# class Struct(format, ...)
#  format: string
#  ...: any type
#  returns: instance of Struct

# Struct.format
#  returns: string

# Struct.size
#  returns: int

# Struct.pack(v1, v2, ...)
#  v1, v2: any type
#  returns: bytes

# Struct.unpack(buffer)
#  buffer: bytes
#  returns: tuple

# Struct.unpack_from(buffer, offset=0)
#  buffer: bytes
#  offset: int
#  returns: tuple


# The struct module has two different API styles. The original API is
# available for compatibility reasons, but you should use the new API for
# all new code.
# https://docs.python.org/3/library/struct.html
# https://www.programiz.com/python-programming/modules/struct
# https://docs.python.org/3/library
