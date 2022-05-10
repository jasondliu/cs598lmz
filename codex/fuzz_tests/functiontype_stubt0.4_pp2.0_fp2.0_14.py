from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(hasattr(a, '__next__'))
print(hasattr(a, '__iter__'))

print(next(a))
print(next(a))

print(a.__next__())
print(a.__next__())

print(a.__iter__())
print(a.__iter__())

print(iter(a))
print(iter(a))

print(list(a))
print(list(a))

print(a.__next__())
print(a.__next__())

print(next(a))
print(next(a))

print(a.__next__())
print(a.__next__())

print(a.__
