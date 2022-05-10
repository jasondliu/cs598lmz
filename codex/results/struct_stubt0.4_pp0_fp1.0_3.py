from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2H'
s.size = s.calcsize(s.format)
print(s.size)

# 使用struct模块定义了一个结构，并且使用pack()方法将数据打包，得到一个bytes对象。
# 可以使用unpack()方法将其解压，得到一个元组，其中的元素就是原始的数据。
# 如果要让结构体变得更加通用，可以使用一个类来实现，这样就可以将结构体的定义和
