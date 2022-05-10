import types
types.MethodType(func, 'obj')
# <method 'func' of 'str' objects>

# 但是，如果对实例进行操作，就能添加动态属性
class Student(object):
    pass
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
s.age

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,
