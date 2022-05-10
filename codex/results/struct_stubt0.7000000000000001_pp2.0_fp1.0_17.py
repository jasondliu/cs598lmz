from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=HBB')
#s.pack(1, 2, 3)
#s.unpack(b'\x01\x02\x03')
#s.unpack_from(b'\x01\x02\x03\x04')
#s.iter_unpack(b'\x01\x02\x03\x04\x05\x06')
s.format = '<hhl'
s.size = 8
s.pack_into(b'\x00' * 8, 0, 1, 2, 3)
s = Struct('!HBB')
s.pack(1, 2, 3)
s.unpack(b'\x01\x02\x03')
s.unpack_from(b'\x01\x02\x03\x04')
s.iter_unpack(b'\x01\x02\x03\x04\x05\x06')
s.format = '<hhl'
s.size
s.pack_into(b'\x00' * 8
