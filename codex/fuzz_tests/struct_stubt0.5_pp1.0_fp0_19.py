from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack(b'\x00\x01')

# from _struct import pack
# pack('<h', 1)

# from _struct import unpack
# unpack('<h', b'\x00\x01')

# from _struct import calcsize
# calcsize('<h')

# from _struct import pack_into
# buf = bytearray(16)
# pack_into('<h', buf, 0, 1)

# from _struct import unpack_from
# buf = bytearray(b'\x00\x01\x00\x02')
# unpack_from('<hh', buf, 0)

# from _struct import Struct
# s = Struct('<h')
# s.pack(1)

# from _struct import Struct
# s = Struct('<h')
# s.unpack(b'\x00\x01')

# from _struct import Struct
# s = Struct('<h')
# s.size

#
