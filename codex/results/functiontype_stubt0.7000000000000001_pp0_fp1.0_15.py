from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())
print(a.__next__())

def func():
    yield 1

print(func())
print(type(func()))
print(isinstance(func(), types.GeneratorType))
