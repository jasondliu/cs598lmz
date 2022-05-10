from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

def f():
    yield 1

print(isinstance(f(), FunctionType))
print(isinstance(f(), GeneratorType))

print(type(f))
print(isinstance(f, FunctionType))
print(isinstance(f, GeneratorType))
