from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断是否是某种类型可以用isinstance()判断：
print(isinstance(a, types.GeneratorType))

# 使用dir()
print(dir('abc'))

# 实例属性和类属性
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
    __slots__ = ('name', 'age') # 用tuple定义允
