from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 打包
s.pack(1)
s.pack(1)
s.pack(1)
s.pack(1)

# 解包
s.unpack(b'\x01\x00\x00\x00')

# 打包
s.pack_into(b'\x00'*4, 0, 1)

# 解包
s.unpack_from(b'\x01\x00\x00\x00', 0)

# 打包
s.pack_into(b'\x00'*4, 0, 1)
s.pack_into(b'\x00'*4, 4, 2)
s.pack_into(b'\x00'*4, 8, 3)
s.pack_into(b'\x00'*4, 12, 4)

# 解包
