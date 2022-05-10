from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

a = map(lambda x: x, [1])
print(type(a))
print(isinstance(a, FunctionType))

a = [x+1 for x in range(5)]
print(type(a))
print(isinstance(a, ListType))
