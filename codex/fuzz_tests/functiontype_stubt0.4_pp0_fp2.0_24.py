from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(id(a), id(b))
print(type(a), type(b))
print(FunctionType, type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, type(b)))
print(isinstance(a, type(a)))
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a,
