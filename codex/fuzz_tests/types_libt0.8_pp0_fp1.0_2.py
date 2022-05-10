import types
types.MethodType(a,b)

def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
s.age

def set_score(self,score):
    self.score = score
Student.set_score = MethodType(set_score,Student)

s.set_score(100)
s.score

s2 = Student('Bob',50)
s2.set_score(60)
s2.score

class Student(object):
    __slots__ = ('name','age')    #使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9
