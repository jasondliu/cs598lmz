from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a) == types.GeneratorType)

print(isinstance(a, types.GeneratorType))
print(isinstance(abs, FunctionType))
print(isinstance(a, types.GeneratorType))
print(isinstance(lambda x: x, types.LambdaType))

import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(isinstance(fn, types.FunctionType))
print(isinstance(fn, types.BuiltinFunctionType))


import types
print(isinstance(types, types.ModuleType))

print(isinstance(123, types.IntType))

print(isinstance('str', types.StringType))

print(isinstance(u'unicode', types.UnicodeType))

def fn():
    pass
print(isinstance(fn, types.FunctionType))

class Animal(object):
    def __init__(self):
        pass
class Dog(Animal):
    def __init__(self):
        pass

dog =
