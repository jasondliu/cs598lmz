from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {1:2}
d = '123'
e = 123
f = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))
print(isinstance(e, GeneratorType))
print(isinstance(f, GeneratorType))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(e, Iterable))
print(isinstance(f, Iterable))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))

