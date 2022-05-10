import types
types.MethodType(f,None,A)

#给实例绑定一个方法：
def set_age(self,age):
    self.age=age

from types import MethodType
a.set_age=MethodType(set_age,a)
a.set_age(25)
a.age

#给一个实例绑定的方法，对另一个实例是不起作用的：
b=A()
b.set_age(25)

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score=score

