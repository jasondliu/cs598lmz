from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(print))
print(type(FunctionType))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(print, Iterator))
print(isinstance(FunctionType, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(print, Iterable))
print(isinstance(FunctionType, Iterable))

print(isinstance(a, Generator))
print(isinstance(b, Generator))
print(isinstance(print, Generator))
print(isinstance(FunctionType, Generator))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(print, FunctionType))
print(isinstance(FunctionType, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(print, list))
print(isinstance(FunctionType,
