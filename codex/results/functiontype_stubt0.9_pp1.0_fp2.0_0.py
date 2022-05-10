from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Generator))
# print(isinstance(a, GeneratorIter))
a = 3
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
a = [x for x in [1]]
print(isinstance(a, Iterator))  # is list an Iterator?
print(isinstance(a, Iterable))
a = [1, 2, 3]
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
a = map(lambda x: x, [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(map, FunctionType))
print(isinstance(map(lambda x: x, [1]), Iterator))  # map is also an Iterator
print(isinstance(map(lambda x: x, [1]), Iter
