from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def foo():
    yield 1
    yield 2
    yield 3

g = foo()
print(type(g))
print(isinstance(g, GeneratorType))
print(isinstance(g, FunctionType))
