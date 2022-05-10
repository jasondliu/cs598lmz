from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
s.size

# 构建一个结构体对象，然后将其包装到一个字节字符串中，最后打印出来看看。
s = Struct('i?f')
data = s.pack(1, False, 2.7)
print(data)

# 现在，我们来解压这个字节字符串，并将解压出来的数据存储到一个元组中
print(s.unpack(data))

# 如果你想将结构体打包成一个字节数组，可以使用 bytes
