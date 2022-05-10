from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

def foo():
    yield 1

b = foo()
print(isinstance(b, FunctionType))

def bar():
    pass

c = bar()
print(isinstance(c, FunctionType))

d = (x for x in [1])
print(isinstance(d, FunctionType))

print(isinstance(d, (FunctionType, GeneratorType)))

print(isinstance(d, (GeneratorType, FunctionType)))

print(isinstance(bar, FunctionType))

print(isinstance(bar, GeneratorType))

print(isinstance(foo, FunctionType))

print(isinstance(foo, GeneratorType))
