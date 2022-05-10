from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Object))

b = (x for x in [1, 2, 3])
print(type(b))
print(isinstance(b, FunctionType))
print(isinstance(b, GeneratorType))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Object))

c = [x for x in [1, 2, 3]]
print(type(c))
print(isinstance(c, FunctionType))
print(isinstance(c, GeneratorType))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, Object))

d = {x for x in [1, 2, 3]}
print(type(d))
print(isinstance(d, FunctionType))
print(isinstance(
