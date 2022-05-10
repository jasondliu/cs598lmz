from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('\n')

def func():
    yield 1

b = func()
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print('\n')

def func():
    yield 1
    yield 2
    yield 3

c = func()
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))

print('\n')

def func():
    yield 1
    yield 2
    yield 3

d = func()
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))

print('\n')

def func():
    yield 1
    yield 2
    yield 3

e = func()
print(type(e))
print(isinstance(e, GeneratorType))
print(isinstance(e, Function
