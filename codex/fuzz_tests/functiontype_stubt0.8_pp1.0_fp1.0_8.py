from types import FunctionType
a = (x for x in [1])
b = [1, 2]
print isinstance(a, Iterator)
print isinstance(b, Iterator)

print isinstance(a, Iterable)
print isinstance(b, Iterable)

print isinstance(a, FunctionType)
print isinstance(b, FunctionType)
