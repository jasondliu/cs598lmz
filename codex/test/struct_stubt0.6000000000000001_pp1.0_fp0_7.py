from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=', 'i')  # '=' means native endian and 'i' means int
s.size             # 4
s.pack(42)         # b'*\x00\x00\x00' (42 as big-endian integer)
s.unpack(b'*\x00\x00\x00')   # (42,)
s.unpack_from(b'@\x00\x00\x00*\x00\x00\x00', 4)   # (42,)

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=', 'i')  # '=' means native endian and 'i' means int
s.size             # 4
s.pack(42)         # b'*\x00\x00\x00' (42 as big-endian integer)
s.unpack(b'*\x00\x00\x00')   # (42,)
