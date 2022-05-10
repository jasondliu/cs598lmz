from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('-' * 30)

def a():
    yield 1

b = a()
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print('-' * 30)

def a():
    yield 1
    return

b = a()
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print('-' * 30)

def a():
    yield 1
    return 1

b = a()
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
