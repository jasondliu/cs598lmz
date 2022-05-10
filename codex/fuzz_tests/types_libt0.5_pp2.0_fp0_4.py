import types
types.MethodType(lambda self, n: n+1, None, int)

# 创建一个类，创建一个实例
class Student(object):
    pass

# 动态绑定属性
s = Student()
s.name = 'Michael'
print(s.name)

# 动态绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(25)

# 为了给所有实
