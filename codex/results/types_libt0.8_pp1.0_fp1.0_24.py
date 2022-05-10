import types
types.MethodType(func,object)

class Student(object):
    pass

s = Student()
s.name = 'michale'
print s.name

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Student)
#s.set_age(25)

s2 = Student()
#s2.set_age(25)

def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,None,Student)

s3 = Student()
s3.set_score(100)
print s3.score
