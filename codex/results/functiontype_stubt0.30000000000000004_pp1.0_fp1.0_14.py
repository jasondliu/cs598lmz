from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print('\n')

def f():
    yield 1
    yield 2
    yield 3

a = f()
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print('\n')

def f():
    return 1
    return 2
    return 3

a = f()
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print('\n')

def f():
    return 1
    yield 2
    yield 3

a = f()
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print('\n')

def f():
    yield 1
    return 2
    yield 3

a = f
