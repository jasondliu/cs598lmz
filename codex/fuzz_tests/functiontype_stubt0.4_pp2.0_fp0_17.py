from types import FunctionType
a = (x for x in [1])
b = [1]
c = 1
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, object))
print(isinstance(b, object))
print(isinstance(c, object))

print(isinstance(a, type))
print(isinstance(b, type))
print(isinstance(c, type))

print(isinstance(a, str))
print(
