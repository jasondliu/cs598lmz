import types
types.MethodType

def set_age(self,age):
    self.age=age

s.set_age=types.MethodType(set_age,s)

s.set_age(25)
s.age

def set_score(self,score):
    self.score=score

Student.set_score=types.MethodType(set_score,Student)

s.set_score(100)
s.score

s2=Student()
s2.set_score(999)
s2.score

class Student(object):
    __slots__=('name','age')

s=Student()
s.name='Michael'
