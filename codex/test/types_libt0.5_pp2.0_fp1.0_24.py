import types
types.MethodType(method, object)

# 给实例绑定的方法，对另一个实例是不起作用的：
class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
