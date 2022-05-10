import types
types.MethodType(func, None, class_name)

# 为实例绑定属性
def set_age(self, age):
    self.age = age

from types import MethodType
class_name.set_age = MethodType(set_age, class_name)

class_name.set_age(25)
class_name.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
class_name2 = class_name('Bob', 20)
class_name2.age

# 为所有实例绑定属性
class_name.set_age = MethodType(set_age, None, class_name)

