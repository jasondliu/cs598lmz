from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, type))
print(isinstance(a, object))

print('*'*30)

print(issubclass(Iterator, Iterable))
print(issubclass(Iterator, Generator))
print(issubclass(Iterator, FunctionType))
print(issubclass(Iterator, type))
print(issubclass(Iterator, object))
