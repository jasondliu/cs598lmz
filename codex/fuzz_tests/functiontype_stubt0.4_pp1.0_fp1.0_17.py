from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type((x for x in [1])))

print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))

print(dir(a))
print(dir(b))
print(dir(abs))
print(dir(lambda x: x))

print(dir('ABC'))
print(dir(123))
print(dir([]))
print(dir({}))

print(hasattr('ABC', '__iter__'))
print(hasattr('ABC', '__len__'))
print(hasattr([], '__iter__'))
print(hasattr([], '__len__'))

print(
