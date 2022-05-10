from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

from types import MethodType
def set_age(self, age):
    self.age = age
    
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
s2 = Student()
s2.set_age(25)

def add_score(self, score):
    self.score = score
Student.set_score = add_score
s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = 'Bob'
s.age = 25

