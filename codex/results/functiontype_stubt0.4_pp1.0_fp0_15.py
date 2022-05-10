from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, Generator))

c = {x: x for x in [1]}
print(type(c))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, Generator))

d = {x for x in [1]}
print(type(d))
print(isinstance(d, Iterator))
print(isinstance(d, Iterable))
print(isinstance(d, Generator))

e = (x for x in [1])
print(type(e))
print(isinstance(e, Iterator))
print(isinstance(e, Iterable))
print(isinstance(e, Generator))

f = FunctionType()
print(
