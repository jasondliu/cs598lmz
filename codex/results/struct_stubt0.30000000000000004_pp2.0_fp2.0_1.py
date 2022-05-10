from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 可以用from_buffer()方法把缓冲区中的二进制数据解析为一个结构体
buffer = bytes(array('i', [7, 8, 9]))
s = Struct('i')
s.size
s.unpack_from(buffer, 0)
s.unpack_from(buffer, 4)
s.unpack_from(buffer, 8)

# 如果要在缓冲区中填充结构体，可以使用pack_into()方法
buffer = bytearray(s.size * 3)
s.pack_into(buffer, 0, 7)
s.pack_into(buffer, s.size, 8)
s.pack_into(buffer, s.size * 2, 9)
buffer

# 如
