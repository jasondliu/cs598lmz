from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断一个对象是否是函数
print(callable(a.__next__))

# 使用dir()
print(dir(a))

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
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 
