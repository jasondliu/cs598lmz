import types
types.MethodType(f, None, Student)

# 实例属性和类属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

# 给实例绑定一个方法：
def set_age(self, age):
    self.age = age

from types import MethodType
s = Student('Bob')
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
