from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

print(type(lambda x: x))
print(type(abs))
print(type(FunctionType))

print(type(a) == type((x for x in range(10))))
print(type(a) == types.GeneratorType)

print(isinstance(a, types.GeneratorType))
print(isinstance((x for x in range(10)), types.GeneratorType))
print(isinstance((x for x in range(10)), types.GeneratorType))
print(dir(a))

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

