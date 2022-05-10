import types
types.MethodType(lambda self: None, None, None)
 
# 定义一个类
class Student(object):
    pass
 
# 实例化一个叫s的对象
s = Student()
# 给实例绑定一个属性
s.name = 'Michael'
print(s.name)
 
# 给实例绑定一个方法
def set_age(self, age):
    self.age = age
 
# 给实例绑定一个方法
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
 
# 给一个实例绑定的方法，对另一个实例是不起作用的
s2
