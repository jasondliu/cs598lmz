from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'QQQQQQQQ'
s.size = 64
print(s.size)

# 创建一个类，并且让它的一个实例拥有自己的属性和方法
class Student(object):
    pass

# 创建实例
s = Student()
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

