import types
types.MethodType(f, None, class_name)

class_name.f()

# 定义一个类
class Student(object):
    pass

# 定义一个对象
s = Student()

# 给对象绑定一个属性
s.name = 'Michael'
print(s.name)

# 给对象绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#
