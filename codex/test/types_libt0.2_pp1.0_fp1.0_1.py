import types
types.MethodType(lambda self: None, None, object)

# TypeError: unbound method __init__() must be called with object instance as first argument (got nothing instead)

# 但是如果我们要给一个实例绑定的方法，可以直接在实例上绑定

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
