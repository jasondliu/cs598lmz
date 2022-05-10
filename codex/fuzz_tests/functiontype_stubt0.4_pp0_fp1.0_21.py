from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

print(type(abs))
print(type(a))
print(type(123))
print(type(None))

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

print(dir('ABC'))

class MyObject(object):
    def __init__(self):
        self
