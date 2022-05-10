from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 使用struct模块的pack函数将Python的值打包成二进制数据
s.pack(1)

# 使用unpack函数将二进制数据解压缩为Python值
s.unpack(_)

# 可以使用标准的格式说明符来指定解压的格式
s = Struct('>I 2s f')
s.size

# 格式说明符'<'表示小端法，'>'表示大端法
s.pack(b'abc')

# 格式说明符'2s'表示2个字节的
