from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

def b():
    print('b')
    yield 1

print(type(b))
print(isinstance(b(), GeneratorType))

print(type(b) == FunctionType)
