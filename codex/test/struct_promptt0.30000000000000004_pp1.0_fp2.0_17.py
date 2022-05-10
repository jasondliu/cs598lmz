import _struct
# Test _struct.Struct

# _struct.Struct is a factory function that returns a subclass of
# _struct.StructType.  The subclass has the following methods:
#
# - pack(v1, v2, ...) -> bytes
# - unpack(bytes) -> (v1, v2, ...)
# - iter_unpack(bytes) -> iterator over (v1, v2, ...)
# - unpack_from(buffer, offset=0) -> (v1, v2, ...)
# - iter_unpack_from(buffer, offset=0) -> iterator over (v1, v2, ...)
# - size
#
# The first argument to the factory function is a format string,
# composed of the following type characters:
#
# Format  C Type             Python type         Standard size
# x       pad byte           no value
# c       char               bytes of length 1   1
# b       signed char        integer             1
# B       unsigned char      integer             1
# ?       _Bool              bool                1
# h       short              integer             2
# H       unsigned short     integer             2

