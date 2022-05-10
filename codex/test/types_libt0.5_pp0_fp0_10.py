import types
types.MethodType(func, obj)

# __slots__魔法
# 定义了__slots__变量，则只允许实例添加__slots__定义的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99

