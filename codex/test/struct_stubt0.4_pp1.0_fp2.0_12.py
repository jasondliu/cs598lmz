from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=2s2s2s2s')
s.size

s.pack('abcd')

s.unpack(b'abcd')

s.unpack(b'abce')

s.unpack(b'abc')

s.unpack(b'abcde')

s.unpack(b'abcdef')

s.unpack(b'abcdefg')

s.unpack(b'abcdefgh')

s.unpack(b'abcdefghi')

s.unpack(b'abcdefghij')

s.unpack(b'abcdefghijk')

s.unpack(b'abcdefghijkl')

s.unpack(b'abcdefghijklm')

s.unpack(b'abcdefghijklmn')

s.unpack(b'abcdefghijklmno')

s.unpack(b'abcdefghijklmnop')

