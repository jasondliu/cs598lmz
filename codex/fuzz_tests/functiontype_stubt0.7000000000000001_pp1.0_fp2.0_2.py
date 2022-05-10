from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))

b = iter([1])
print(isinstance(b, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(isinstance(a, Generator))
print(isinstance(b, Generator))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
