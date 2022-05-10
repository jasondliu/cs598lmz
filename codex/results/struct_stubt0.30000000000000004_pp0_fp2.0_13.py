from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 可以用来创建空的类
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# 可以用来创建空的类
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# 可以用来创建空的类
class MyMeta(type):
    def __new__(cls, name, bases,
