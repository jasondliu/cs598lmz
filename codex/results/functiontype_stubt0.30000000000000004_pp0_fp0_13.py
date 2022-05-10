from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))

print(isinstance(a.__iter__, FunctionType))
print(isinstance(a.__next__, FunctionType))
print(isinstance(a.send, FunctionType))
print(isinstance(a.throw, FunctionType))
print(isinstance(a.close, FunctionType))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

print(issubclass(Iterator, Iterable))
print(issubclass(Iterator, Generator))
print(issubclass(Iterator, object))

print(issubclass(Generator, Iterable))
print(issubclass(Generator, object))

print(issubclass(Iterable, object))

print(issubclass(object, Iterable))

print(issubclass(object
