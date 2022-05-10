from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1])
print(b)
print(type(b))

print(a is b)

def func():
    yield 1
    yield 2
    yield 3

print(type(func))

print(type(func()) is type(b))
print(type(func()) is type(a))
print(type(func) is FunctionType)

print(isinstance(func, FunctionType))
print(isinstance(func(), GeneratorType))

print(isinstance(func, (FunctionType, GeneratorType)))
print(isinstance(func(), (FunctionType, GeneratorType)))

print(isinstance(func, (FunctionType, GeneratorType, int)))
print(isinstance(func(), (FunctionType, GeneratorType, int)))
