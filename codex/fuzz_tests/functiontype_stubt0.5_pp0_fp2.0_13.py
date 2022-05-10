from types import FunctionType
a = (x for x in [1])
print(type(a))

def foo():
    yield 1
    yield 2

print(type(foo))
print(type(foo()))

print(isinstance(a,GeneratorType))
print(isinstance(foo,FunctionType))
print(isinstance(foo(),GeneratorType))
