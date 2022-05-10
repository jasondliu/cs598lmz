from types import FunctionType
list(FunctionType(lambda x: x+1, {}).__globals__.keys())

# MethodType
# MethodType(function, instance, class)
#   function: the function object to be bound
#   instance: the instance to which the function is to be bound
#   class: the class to which the instance belongs

from types import MethodType

class A:
    def __init__(self, name):
        self.name = name

a = A('Bob')
a.get_name = MethodType(lambda self: self.name, a)
print(a.get_name())

# 可以通过类的方法名绑定方法
class B:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

b = B('Tom')
b.get_name = MethodType(lambda self: self.name, b, B)
print(b.get_name())

# MethodDescriptorType
# FunctionType and Method
