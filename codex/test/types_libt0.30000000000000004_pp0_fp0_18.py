import types
types.MethodType(f, None, Student)

# 使用__slots__限制class的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
