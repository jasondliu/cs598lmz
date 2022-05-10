from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

print(isinstance(f, FunctionType))
print(isinstance(g, FunctionType))
print(isinstance(h, FunctionType))

print(isinstance(f, GeneratorType))
print(isinstance(g, GeneratorType))
print(isinstance(h, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(f, GeneratorType))
print(isinstance(g, GeneratorType))
print(isinstance(h, GeneratorType))

print(isinstance(f, FunctionType))
print(isinstance(g, FunctionType))
print(isinstance(h
