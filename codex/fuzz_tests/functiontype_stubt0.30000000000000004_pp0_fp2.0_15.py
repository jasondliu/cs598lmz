from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == IteratorType)
print(type(a) == IterableType)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(a, (IteratorType, IterableType)))

print(isinstance(a, (GeneratorType, IteratorType, IterableType)))

print(isinstance(a, (GeneratorType, IteratorType, IterableType, FunctionType)))

print(isinstance(a, (GeneratorType, IteratorType, IterableType, FunctionType, type(None))))

print(isinstance(a, (GeneratorType, IteratorType, IterableType, FunctionType, type(None), int)))

print(isinstance(a, (
