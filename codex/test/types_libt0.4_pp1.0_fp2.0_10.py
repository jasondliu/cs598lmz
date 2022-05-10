import types
types.MethodType(f, None, None)

# 我们也可以使用types.MethodType() 动态地给一个实例绑定一个方法
# 请看示例：

class Student(object):
    pass

s = Student()

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法
# 请看示例
