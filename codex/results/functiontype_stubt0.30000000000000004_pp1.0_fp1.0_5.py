from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))

c = {x for x in [1]}
print(type(c))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))

d = {x: x for x in [1]}
print(type(d))
print(isinstance(d, Iterator))
print(isinstance(d, Iterable))

e = {x for x in [1]}
print(type(e))
print(isinstance(e, Iterator))
print(isinstance(e, Iterable))

f = FunctionType
print(type(f))
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))

g = (x for x in [1])
print(type(g))
print(isinstance(
