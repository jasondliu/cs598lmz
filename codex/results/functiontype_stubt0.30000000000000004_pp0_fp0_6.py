from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, object))

print('-' * 30)

b = [1, 2, 3]
print(b)
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, object))

print('-' * 30)

c = (x for x in [1, 2, 3])
print(c)
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, object))

print('-' *
