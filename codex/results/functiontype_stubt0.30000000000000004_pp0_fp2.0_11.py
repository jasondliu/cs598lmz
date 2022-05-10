from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

print(isinstance(a, Generator))
print(isinstance(b, Generator))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
