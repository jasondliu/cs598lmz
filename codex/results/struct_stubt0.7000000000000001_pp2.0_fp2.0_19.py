from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>1s1s1s1s', '>')
s.pack(b'A', b'B', b'C', b'D')

'''
4.4 处理原始的字节

1. 内存视图
类似于数组，用于修改字节的内容，支持类型转换。

2. 字节数组
类似于列表，可修改字节内容，不支持类型转换。

3. bytes 
类似于字符串，不可修改字节内容，支持
