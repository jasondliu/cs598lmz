from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, type(b)))
print(isinstance(b, type(a)))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

print(isinstance(a, IteratorType))
print(isinstance(b, IteratorType))

print(isinstance(a, IterableType))
print(isinstance(b, IterableType))

print(isinstance(a, IteratorType))
print(isinstance(b, IteratorType))

print(isinstance(a, IterableType))
print(isinstance(b, IterableType))

print(isinstance(a, IteratorType))
print(isinstance(b, IteratorType))

print(isinstance(a, IterableType
