from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(abs, FunctionType))
print(isinstance(abs, GeneratorType))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, GeneratorType))

print(isinstance(x for x in [1], FunctionType))
print(isinstance(x for x in [1], GeneratorType))

print(isinstance(map(lambda x: x, [1]), FunctionType))
print(isinstance(map(lambda x: x, [1]), GeneratorType))

print(isinstance(map(lambda x: x, [1]), Iterator))
print(isinstance(map(lambda x: x, [1]), Iterable))

print(isinstance(map(lambda x: x, [1]), Iterator))
print(isinstance(map(lambda x: x, [1]), Iterable))

print(isinstance(map(lambda x: x, [1]), Iterator))
print(is
