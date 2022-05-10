from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# pack
s.pack(1, b'ab', 2.7)

# unpack
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\x08@')

# pack with keywords
s.pack(sequence_number=1, tag='ab', value=2.7)

# unpack with keywords
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\x08@',
         sequence_number=1, tag='ab', value=2.7)

# unpack with keywords and names
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99
