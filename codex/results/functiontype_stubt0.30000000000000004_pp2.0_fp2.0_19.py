from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

def f():
    yield 1

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

def f():
    return 1

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f()) == GeneratorType)

print(type(f) == FunctionType)
print(type(f())
