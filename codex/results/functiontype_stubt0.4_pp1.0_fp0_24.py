from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [x for x in [1]]
print(type(b))
c = {x for x in [1]}
print(type(c))
d = {x:x for x in [1]}
print(type(d))
e = FunctionType(lambda x:x, globals())
print(type(e))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))
print(isinstance(e, GeneratorType))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))
print(isinstance(e, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(e, Iterable))

print
