import types
types.MethodType(m, None)

#%%
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

#%%
s2 = Student()
# s2.set_age(25)

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2.set_score(99)
s2.score

#%%
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

#%%
class Student(object):
    pass

s = Student()
s.name = 'Michael'
