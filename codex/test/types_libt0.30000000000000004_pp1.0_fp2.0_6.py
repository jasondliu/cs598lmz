import types
types.MethodType(lambda self: self.name, None, Person)

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
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
print(g.score)

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
print(g.score)

