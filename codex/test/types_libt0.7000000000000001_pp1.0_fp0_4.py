import types
types.MethodType

class Student(object):
    pass

s1 = Student()
def set_age(self, age):
    self.age = age

from types import MethodType
s1.set_age = MethodType(set_age, s1)
s1.set_age(25)
s1.age

s2 = Student()
#s2.set_age(25)
s2.set_age = MethodType(set_age, s2)
s2.set_age(25)

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)
s1.set_score(100)
s1.score
s2.set_score(99)
s2.score

# __slots__
class Person(object):
    __slots__ = ('name', 'gender')

p1 = Person()
p1.name = 'Bob'
p1.gender = 'male'
#p1.score = 88

# 使用__sl
