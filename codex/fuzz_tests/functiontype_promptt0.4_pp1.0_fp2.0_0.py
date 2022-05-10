import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.print_score = types.MethodType(lambda self: print('%s: 99' % self.name), s)
s.print_score()

# Test types.UnboundMethodType
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# Test types.MethodType
s2 = Student('Alice')
# s2.set_age(25) # AttributeError: 'Student' object has no attribute
