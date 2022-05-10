from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
 
s.pack(1, b'ab', 2.7)
s.unpack(_)
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')
 
bp = s.iter_unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')
next(bp)
next(bp)
 
