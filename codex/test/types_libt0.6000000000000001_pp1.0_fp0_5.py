import types
types.MethodType(f, None, Student)
print(Student.name)
print(Student.get_score)

# 使用__slots__
# 限制class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99# AttributeError: 'Student' object has no attribute 'score'

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass
g = GraduateStudent()
