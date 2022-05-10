from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(a, list))

b = [x for x in [1]]
print(b)
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
print(isinstance(b, list))

c = {x for x in [1]}
print(c)
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, Iterable))
print(isinstance(c, Iterator))
print(isinstance(c, list))

d = {x: x for x in [1]}
print(d)
print(type(d))
print(isinstance(d
