import _struct
# Test _struct.Struct

# _struct.Struct(fmt)
# fmt: format string
# return: instance of Struct

# _struct.Struct.format: format string
# _struct.Struct.size: size of struct
# _struct.Struct.pack(v1, v2, ...): return packed bytes
# _struct.Struct.pack_into(buffer, offset, v1, v2, ...): pack into buffer
# _struct.Struct.unpack(buffer): return tuple of values
# _struct.Struct.unpack_from(buffer, offset=0): unpack from buffer

# format string:
# <: little endian
# >: big endian
# !: network (= big-endian)
# x: pad byte
# c: char
# b: signed char
# B: unsigned char
# ?: _Bool
# h: short
# H: unsigned short
# i: int
# I: unsigned int
# l: long
# L: unsigned long
# q: long long
# Q: unsigned long long
# f: float
# d: double
# s: char[]

