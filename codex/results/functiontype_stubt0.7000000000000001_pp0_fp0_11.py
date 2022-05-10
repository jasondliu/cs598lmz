from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x:x))

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(lambda x:x, GeneratorType))
print(isinstance(lambda x:x, FunctionType))


print(dir(a))
