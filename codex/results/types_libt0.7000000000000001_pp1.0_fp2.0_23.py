import types
types.FunctionType

class Student(object):
    __slots__ = ('name','age')
    pass

s = Student()
s.name = 'Michael'
s.age = 25
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)


class GradStudent(Student):
    pass

g = GradStudent()
g.score = 99
print('g.score =', g.score)


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print('s.age =', s.age)


def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print('s.score =', s.score)

s2 = Student()
s2.set_score(99)
print('s2.score =', s2.score)
