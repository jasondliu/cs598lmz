import types
types.MethodType(func, None, type(None))

# TypeError: descriptor '__init__' of 'object' object needs an argument

# 先创建一个空类
class Student(object):
    pass

# 再创建一个实例
s = Student()

# 给实例绑定一个属性
s.name = 'Michael'
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()

