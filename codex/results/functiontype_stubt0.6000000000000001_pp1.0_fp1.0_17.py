from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(range(1)))
print(type(isinstance))
print(type(FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(range(1), GeneratorType))
print(isinstance(isinstance, GeneratorType))
print(isinstance(FunctionType, GeneratorType))

print(isinstance(a, IteratorType))
print(isinstance(b, IteratorType))
print(isinstance(range(1), IteratorType))
print(isinstance(isinstance, IteratorType))
print(isinstance(FunctionType, IteratorType))


print(isinstance(a, IterableType))
print(isinstance(b, IterableType))
print(isinstance(range(1), IterableType))
print(isinstance(isinstance, IterableType))
print(isinstance(FunctionType, IterableType))

print(isinstance(a, IterableType))
print(isinstance(b
