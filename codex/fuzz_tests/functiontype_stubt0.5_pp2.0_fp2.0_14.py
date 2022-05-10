from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('-' * 40)

def f():
    return 1

def g():
    yield 1

print(type(f))
print(type(g))
print(isinstance(f, FunctionType))
print(isinstance(g, FunctionType))
