from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s.pack(1,'xy',3.14)

s.unpack(b'\x01\x00\x00\x00xy\x00\x00\x9a\x99\x99\x99\x99\x99\xf9?')
