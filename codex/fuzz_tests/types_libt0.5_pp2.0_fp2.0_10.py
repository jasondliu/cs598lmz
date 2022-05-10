import types
types.MethodType(f, None, Student)

#改变一个实例的属性
s = Student()
s.name = 'Michael'
print(s.name)

#给实例绑定一个方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25)

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score
