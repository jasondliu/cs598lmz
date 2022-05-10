from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
from collections import Iterable, Iterator
print(callable(a))
print(callable(abs))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 使用dir()
print(dir('ABC'))

# 类属性和实例属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

# 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定
