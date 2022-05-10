from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def b():
    yield 1
print(isinstance(b(), GeneratorType))
print(isinstance(b(), FunctionType))

def c():
    return 1
print(isinstance(c(), GeneratorType))
print(isinstance(c(), FunctionType))
