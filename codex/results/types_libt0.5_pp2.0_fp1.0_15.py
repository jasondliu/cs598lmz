import types
types.MethodType(func, None, class_name)
# 实例属性和类属性
# 给实例绑定属性
s.name = 'Michael'
# 给实例绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age
# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student('Bob')
s2.set_age(25)
s2.age
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_
