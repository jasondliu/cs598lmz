from types import FunctionType
a = (x for x in [1])
print(a)

def test():
    print('test')

print(type(test))
print(type(test) == FunctionType)

print(type(a))
print(type(a) == FunctionType)

print(type(a) == type(test))

print(type(a) == GeneratorType)

print(isinstance(a, GeneratorType))

print(isinstance(test, FunctionType))

print(isinstance(test, GeneratorType))

print(isinstance(a, FunctionType))
