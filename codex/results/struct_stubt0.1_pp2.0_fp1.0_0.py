from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 可以看到，Struct对象在内部保存了一个格式化字符串和一个转换后的字节序列，
# 当调用unpack()方法时，自动将传入的字节序列按照格式转换为原始数据。

# 小结
# struct模块定义的数据类型可以参考Python官方文档：
# https://docs.python.org/3/library/struct.html#format-characters

#
