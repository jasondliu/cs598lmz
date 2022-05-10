from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a)
print(next(a))

def b():
    yield 1
    yield 2
    yield 3
print(type(b))
print(type(b()))
print(b())
print(next(b()))

print(type(b)==FunctionType)
print(type(b())==GeneratorType)
