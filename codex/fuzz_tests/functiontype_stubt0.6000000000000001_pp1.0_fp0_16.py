from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

def f():
    pass

print(isinstance(f, FunctionType))
print(isinstance(f, GeneratorType))
