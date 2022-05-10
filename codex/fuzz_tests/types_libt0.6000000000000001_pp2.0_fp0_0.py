import types
types.MethodType(t,s)

# 2.给实例绑定一个方法
def set_age(self,age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
s.age

def set_gender(self,gender):
	self.gender = gender

Student.set_gender = set_gender

s.set_gender('M')
s.gender

s2 = Student('Lisa',16)
s2.set_gender('F')
s2.gender
