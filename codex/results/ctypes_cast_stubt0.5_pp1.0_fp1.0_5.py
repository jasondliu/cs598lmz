import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

# 创建一个类
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y', 19)
getattr(obj, 'y')

obj.y

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
s.name
s.name = 'Michael'
s.name
Student.name
del s.name
s.name

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25

# 使用@property
class Student(object
