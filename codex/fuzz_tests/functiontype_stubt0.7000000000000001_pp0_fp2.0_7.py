from types import FunctionType
a = (x for x in [1])
b = iter([1])
c = [1]

print(type(a), type(b), type(c))
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, list))
