from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(x for x in [1]))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(dir(a))
print(dir(abs))
print(dir(lambda x: x))
print(dir((x for x in [1])))
print(dir(x for x in [1]))

print(hasattr(a, '__iter__'))
print(hasattr(a, '__next__'))
print(hasattr(a, '__getitem__'))
print(hasattr(a, '__call__'))

print(hasattr(abs, '__iter__'))
print(hasattr(abs, '__next__'))
print(hasattr(abs, '__getitem__'))
print(hasattr(abs,
