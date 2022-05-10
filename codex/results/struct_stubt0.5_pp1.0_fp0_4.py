from _struct import Struct
s = Struct.__new__(Struct)
data = s.pack(123, b'abc', 1.23)
print(data)
print(list(data))
print(s.unpack(data))

# 这里的Struct类并没有继承自任何类，因此它不是一个真正的类。
# 它是一个类的实例，只是这个实例的类是Struct类。
# 这种用法允许创建出简单的数据处理对象来替代常见的lambda表达式。

# 下面是一个示例，它接受一个浮点数并返回一个字
