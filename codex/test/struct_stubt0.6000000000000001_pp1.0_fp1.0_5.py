from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!I', 4)
s

s.pack(2)

s.pack_into(buffer(b'abc'), 1, 3)
b'abc'

s.unpack_from(buffer(b'abc'), 1)
(3,)

s.unpack(b'\x00\x00\x00\x03')
(3,)

s.calcsize()
4

s = Struct.__new__(Struct)
s.__init__('!I4s')
s

s.pack(3, b'xyz')
b'\x00\x00\x00\x03xyz'

s.pack_into(b'abcdef', 2, 5, b'xyz')
b'abcxyzef'

s.unpack(b'\x00\x00\x00\x05xyz')
(5, b'xyz')

s.unpack_from(b'abcxyzef', 3)
(5, b'xyz')

s.calcs
