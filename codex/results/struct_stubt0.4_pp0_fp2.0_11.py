from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2s2sif")
print(s.size)
print(s.pack("AB", b"\x01", b"\x02", 3, 4.0))
print(s.unpack(b"AB\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00@"))

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2s2sif")
print(s.size)
print(s.pack("AB", b"\x01", b"\x02", 3, 4.0))
print(s.unpack(b"AB\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00@"))

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2s2sif")
print(s.size)
print(s.pack("AB", b"\x01", b
