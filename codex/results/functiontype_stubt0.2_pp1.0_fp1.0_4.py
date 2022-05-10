from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

def b():
    yield 1

print(b)
print(type(b))
print(type(b) == GeneratorType)
print(type(b) == FunctionType)

print(type(b()) == GeneratorType)
print(type(b()) == FunctionType)
