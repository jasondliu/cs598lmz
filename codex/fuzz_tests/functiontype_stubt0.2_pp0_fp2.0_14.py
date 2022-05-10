from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a,FunctionType))
print(isinstance(a,GeneratorType))

print(type(a) == GeneratorType)
print(type(a) == FunctionType)
