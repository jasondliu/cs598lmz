import types
types.MethodType(f, None, Student)

f.__name__

def set_age(self, age):
  self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

#一个类的实例只能绑定一个方法，再次绑定后，前一个会被覆盖。
#给一个实例绑定方法，对另一个实例是不起作用的。

s2 = Student('Bob', 18)
s2.set_age(25)

#为了给所有实例都绑定方法，可以给class绑定方法。
