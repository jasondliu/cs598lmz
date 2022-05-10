from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')
(1,)
s.unpack_from(b'\x01\x00\x00\x00')
(1,)
s.unpack_from(b'\x01\x00\x00\x00', 0)
(1,)
s.unpack_from(b'\x01\x00\x00\x00', 4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.unpack_from(b'\x01\x00\x00\x00', 4)
struct.error: unpack_from requires a buffer of at least 4 bytes
s.unpack_from(b'\x01\x00\x00\x00', 0)
(1,)
s.unpack_from(b'\x01\x00\x00\x00', 1)
Traceback (most recent call last):
  File "<p
