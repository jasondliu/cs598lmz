from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(lambda x:x))
print(type(abs))
print(type(a.__iter__))
print(type(iter(a)))

# isinstance
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, FunctionType))
print(isinstance(a, type))
print(isinstance(a, object))
print(isinstance(a, int))

# dir
print(dir(a))
