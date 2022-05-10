from types import FunctionType
a = (x for x in [1])

print(a)

print(type(a))

print(isinstance(a, Iterator))

print(isinstance(a, Iterable))

print(isinstance(a, FunctionType))

print(isinstance(a, Generator))

a = [1]

print(isinstance(a, Iterator))

print(isinstance(a, Iterable))

print(isinstance(a, FunctionType))

print(isinstance(a, Generator))

a = 1

print(isinstance(a, Iterator))

print(isinstance(a, Iterable))

print(isinstance(a, FunctionType))

print(isinstance(a, Generator))

a = lambda x:x

print(isinstance(a, Iterator))

print(isinstance(a, Iterable))

print(isinstance(a, FunctionType))

print(isinstance(a, Generator))



from collections import Iterable, Iterator, Generator

a = (x for x in [1])

print(isinstance(a
