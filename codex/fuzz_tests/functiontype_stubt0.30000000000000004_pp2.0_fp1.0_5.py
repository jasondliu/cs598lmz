from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def gen():
    yield 1

g = gen()
print(isinstance(g, GeneratorType))
print(isinstance(g, FunctionType))
