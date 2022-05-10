import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

class A(object):
    pass

a = A()
print a.__class__.__name__

# 动态绑定
def set_age(self, age):
    self.age = age

from types import MethodType
a.set_age = MethodType(set_age, a, A)
a.set_age(25)
print a.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
b = A()
# b.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

A.set_score = set_score
