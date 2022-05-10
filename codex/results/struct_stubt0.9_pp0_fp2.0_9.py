from _struct import Struct
s = Struct.__new__(Struct)
#Struct.format = 'I 2s f'
#Struct.__init__(s, '0II0s0s')
getattr(s, 'format')
s.size
s.unpack(b'\x08\x00\x00\x00abc\x00\x00\x00\x00\x00')

s = Struct('I 2s f')
s.pack(1, 'ab', 2.7)

s = Struct('I 2s f')
s = Struct('I 2s f 8p 0I')
s = Struct('I 2s f 0p 0I')
s = Struct('I 2s f 2p 0I')
