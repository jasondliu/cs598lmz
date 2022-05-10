from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')  # big-endian, 16-bit unsigned
a = s.unpack_from(b'\x14\x00', 0)
print(a)

# >>> s = Struct.__new__(Struct)
# >>> s.__init__('>H')
# >>> a = s.unpack_from(b'\x14\x00', 0)
# >>> a
# (20, )
# >>> s.unpack_from(b'\x00\x14', 0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# struct.error: unpack_from requires a buffer of at least 2 bytes
# >>>
