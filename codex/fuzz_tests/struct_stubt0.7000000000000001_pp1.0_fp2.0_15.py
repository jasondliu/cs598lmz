from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

s = Struct('i?f')
s.pack(1, False, 2.3)

s.unpack(_)

s.pack(1, 2.3)

s.unpack(_)

s = Struct('P')
s.pack(b'abc')

s.unpack(_)

s = Struct('P')
s.pack('abc')

s.unpack(_)

s = Struct('P')
s.pack(b'abc', False, 2.3)

s.unpack(_)

s.pack(b'abc', True, 2.3)

s.unpack(_)

s.size

s = Struct('P?f')
s.size

s.pack(b'abc', False, 2.3)

s.unpack(_)

s.pack(b'abc', True, 2.3)

s.unpack(_)

s = Struct
