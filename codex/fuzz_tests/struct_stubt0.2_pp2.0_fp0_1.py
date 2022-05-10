from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1, b'ab', 2.7))

# 使用struct模块的pack函数来打包数据
# 使用unpack函数来解包数据
# 使用pack_into和unpack_from函数来在文件中读写数据
# 使用iter_unpack函数来解压数据

# 使用struct模块的pack函数来打包数据
# pack函数接受一个格式字符串和一系列的原始字节来打包数据
#
