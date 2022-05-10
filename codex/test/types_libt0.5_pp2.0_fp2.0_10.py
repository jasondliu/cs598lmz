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
