from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(abs, FunctionType))
print(isinstance(abs, GeneratorType))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, GeneratorType))

print(isinstance(x for x in [1], FunctionType))
print(isinstance(x for x in [1], GeneratorType))

print(isinstance((x for x in [1]), FunctionType))
print(isinstance((x for x in [1]), GeneratorType))

print(isinstance(int, FunctionType))
print(isinstance(int, GeneratorType))

print(isinstance(int(), FunctionType))
print(isinstance(int(), GeneratorType))

print(isinstance(list, FunctionType))
print(isinstance(list, GeneratorType))

print(isinstance(list(), FunctionType))
print(isinstance(list(), GeneratorType))

print(isinstance(dict, FunctionType))
print(isinstance(dict, GeneratorType))
