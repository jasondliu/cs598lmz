from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
print(a)
print(b)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance([1, 2], Iterable))
print(isinstance(1, Iterable))
print(isinstance('', Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance(True, Iterable))
print(isinstance(None, Iterable))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance([1, 2], Iterator))
print(isinstance(1, Iterator))
print(isinstance('', Iterator))
print(isinstance({}, Iter
