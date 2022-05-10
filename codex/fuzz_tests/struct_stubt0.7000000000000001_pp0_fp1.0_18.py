from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>BH')
s.size

s.pack(1, 2)

s.unpack(b'\x00\x01\x00\x02')

s.pack_into(b'\x00\x00\x00\x00', 3, 1, 2)

s.unpack_from(b'\x00\x00\x00\x01\x00\x02', 3)

fmt = '>BH'
s = Struct(fmt)
s.size
s.unpack(b'\x00\x01\x00\x02')

s = Struct('xx2sI3s')
s.size

s.pack('spam', 42, 'eggs')

s.unpack(b'xxspam\x00\x00\x00*\x00\x00\x00eggs')

s = Struct('>i4sh')
import binascii
raw = binascii.unhexlify('0100000061620000cdcc2
