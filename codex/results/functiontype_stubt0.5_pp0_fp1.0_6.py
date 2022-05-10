from types import FunctionType
a = (x for x in [1])

print(type(a))
print(type(a.__iter__()))
print(type(a.__next__()))
print(type(print))
print(type(lambda x:x))
print(type(x for x in [1]))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance(a.__iter__(), Iterator))
print(isinstance(a.__iter__(), Iterable))
print(isinstance(a.__iter__(), Generator))
print(isinstance(a.__iter__(), FunctionType))

print(isinstance(a.__next__(), Iterator))
print(isinstance(a.__next__(), Iterable))
print(isinstance(a.__next__(), Generator))
print(isinstance(a.__next__(), FunctionType))

print(isinstance(print, Iterator))
print(isinstance(print, Iterable))
print(isinstance(
