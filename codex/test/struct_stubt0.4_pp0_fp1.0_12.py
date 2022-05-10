from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)

# 使用类的实例化方法
class MyStruct(Struct):
    _fields_ = [
        ('I', 'id'),
        ('f', 'height'),
        ('d', 'weight'),
    ]

ms = MyStruct('idf')
print(ms.size)

# 调用类的方法
ms.pack(1, 1.75, 81.2)
print(ms.size)

# 类的属性
print(ms.format)

# 继承类
class Point(Struct):
    _fields_ = [
        ('x', 'i'),
        ('y', 'i'),
    ]

class Circle(Point):
    _fields_ = [
        ('r', 'i'),
    ]

c = Circle.__new__(Circle)
c.__init__('iii')
print(c.size)

# 类的
