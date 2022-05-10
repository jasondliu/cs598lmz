from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 3.14)

# 打包的结果是一个bytes对象
# 解包后会返回一个元组
s.unpack(_)

# 将多个结构体打包在一起
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack_into(b'\x00' * 16, 4, 1, 'ab'.encode('utf-8'), 3.14)

# 将结构体打包到一个文件对象中
with open('data.bin', 'wb') as f:
    s.pack_into(f, 0, 1, 'ab'.encode('utf-8'), 3.14)

# 将
