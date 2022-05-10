from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s.pack(b'123', b'ab', 2.7)
s.unpack(_)
s.unpack(_) == (123, b'ab', 2.7)
s.unpack(b'\x00\x00\x00\x00')
s.unpack(b'\x01\x00\x00\x00abc\x00\x00\x00\x00\x00\x00?\x9a\x99\x99\x99\x99\x99\xf8')

from _struct import unpack
unpack('I 2s f', b'\x01\x00\x00\x00abc\x00\x00\x00\x00\x00\x00?\x9a\x99\x99\x99\x99\x99\xf8')

from _struct import unpack
