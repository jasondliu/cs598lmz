from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(type(a) == GeneratorType)

print(isinstance(list, FunctionType))
print(isinstance(list, type))
print(type(list) == FunctionType)

print(isinstance(dict, FunctionType))
print(isinstance(dict, type))
print(type(dict) == FunctionType)
