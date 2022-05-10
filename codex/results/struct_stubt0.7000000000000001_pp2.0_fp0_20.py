from _struct import Struct
s = Struct.__new__(Struct)
s.size = 20
s.format = '<20s'
fmt = s.format
fmt

# _struct.Struct.format
# Return a string containing the format of this Struct object.

# NOTE: The format string is the same as the format string used in the struct module.

# Appendix: How to use Hexdump

# $ hexdump -C /dev/urandom | head
# 00000000  e7 ef e2 a2 e7 99 4e d8  32 bb f1 f9 d9 a7 9d e8  |.....N.2........|
# 00000010  a1 ef 52 71 1b b9 97 2b  8f b6 a8 e6 e7 f2 e2 cf  |..Rq...+........|
# 00000020  b0 9d a7 ee e8 e7 e0 e1  d6 a7 b6 e8 e6 b7 d9 e4  |................|
# 00000030  9d c2 a6 f0 9d c2 b6 e8  e7 e2 e2 db 9d c2
