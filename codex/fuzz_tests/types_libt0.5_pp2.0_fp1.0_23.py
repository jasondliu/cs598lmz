import types
types.MethodType(f, None, Student)

# __slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25

# 除非在__slots__中，否则不允许绑定其他属性
# s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 除非在子
