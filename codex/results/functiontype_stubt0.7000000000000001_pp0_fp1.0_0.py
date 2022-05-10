from types import FunctionType
a = (x for x in [1])

print(a)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
print(isinstance(a, Generator))
