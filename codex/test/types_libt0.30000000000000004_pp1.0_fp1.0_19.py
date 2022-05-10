import types
types.MethodType(func, None, class_name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
