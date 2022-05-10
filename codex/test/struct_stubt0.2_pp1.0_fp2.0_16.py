from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 可以使用format字符串来指定结构的格式，然后使用pack()或unpack()方法来读写二进制数据
# pack()方法接受一个可以转换为字节的对象序列作为输入，返回一个bytes对象
# unpack()方法接受一个bytes对象以及一个格式字符串作为输入，返回一个解压后的元组
# 如果结构中包含更多的字节
