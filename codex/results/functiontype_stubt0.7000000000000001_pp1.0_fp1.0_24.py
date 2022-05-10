from types import FunctionType
a = (x for x in [1])
b = [1]
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

def f():
    yield 1
g = f()
print(isinstance(g, GeneratorType))
print(isinstance(g, FunctionType))

print(isinstance(f, GeneratorType))
print(isinstance(f, FunctionType))
