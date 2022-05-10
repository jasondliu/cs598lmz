import types
types.MethodType(func, None, type)

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

print(s.age)

def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(100)

print(s.score)

#给一个实例绑定的方法，对另一个实例是不起作用的

s2 = Student()

#s2.set_score(99)

class Student(object):
	__slots__ = ('name', 'age')
	
s = Student()

s.name = 'Michael'
s.age
