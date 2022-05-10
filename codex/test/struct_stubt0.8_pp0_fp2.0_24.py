from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.unpack_from(b"\x01\x02\x03\x04")

# [clinic input]
# _struct.Struct.unpack
#     format: str
#     buffer: Py_buffer
#     /
#
# Unpack bytes using this format string.
# [clinic start generated code]

def unpack(self, format, buffer):
    """Unpack bytes using this format string."""
    return self.__unpack(format, buffer)

# [clinic end generated code: output=2c57e3668db38754 input=f1f7e9582c4f8a0a]

# [clinic input]
# _struct.Struct.unpack_from
#     format: str
#     buffer: Py_buffer
#     offset: int = 0
#     /
#
# Unpack bytes from a buffer starting from a given offset, using this format string.
# [clinic start generated code]

