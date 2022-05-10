import types
types.MethodType(foo, obj)

# 关于__slots__
# 用tuple定义允许绑定的属性名称
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

