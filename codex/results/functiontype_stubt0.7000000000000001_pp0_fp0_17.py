from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a), type(b), type(a)==type(b))
print(type(a)==FunctionType)
print(type(a)==GeneratorType)
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

print(dir(a))
print(dir(b))

print(hasattr(a, '__next__'))
print(hasattr(a, '__iter__'))
print(hasattr(a, '__contains__'))
print(hasattr(b, '__contains__'))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

print(isinstance(a, Container))
print(isinstance(b, Container))

print(isinstance(a, Sized))
print(isinstance(b, Sized))

print(isinstance(a, Sequence))
print(is
