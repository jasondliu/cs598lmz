import types
types.MethodType(f,None,Foo) # 把函数变成实例方法

# 给实例绑定一个方法
def set_age(self,age):
    self.age = age
from types import MethodType
f = Foo()
f.set_age = MethodType(set_age,f)
f.set_age(25)
print(f.age)

#给所有实例绑定方法
Foo.set_age = set_age
f1 = Foo()
f2 = Foo()
f1.set_age(25)
f2.set_age(26)
print(f1.age,f2.age)

# 限制类属性
class Student(object):
    __slots__ = ('name','age','sex','grade') # 用tuple定义允许绑定的属性
