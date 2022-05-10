from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(x for x in [1]))

print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))

print(dir(a))

print(hasattr(a, '__next__'))
print(hasattr(a, '__iter__'))
print(hasattr(a, '__getitem__'))
print(hasattr(a, '__call__'))

print(getattr(a, '__next__'))
print(getattr(a, '__iter__'))
print(getattr(a, '__getitem__'))
print(getattr(a, '__call__'))
