from types import FunctionType
a = (x for x in [1])

print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print('\n')

def b():
    yield 1

print(b)
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
