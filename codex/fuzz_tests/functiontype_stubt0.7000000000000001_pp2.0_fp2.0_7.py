from types import FunctionType
a = (x for x in [1])
b = {x for x in [1]}
c = {1:1}
d = [1, 2]
e = iter(range(3))
f = "ab"
g = FunctionType(lambda: None, globals())
h = object()
print(isinstance(a, collections.abc.Iterable))
print(isinstance(b, collections.abc.Iterable))
print(isinstance(c, collections.abc.Iterable))
print(isinstance(d, collections.abc.Iterable))
print(isinstance(e, collections.abc.Iterable))
print(isinstance(f, collections.abc.Iterable))
print(isinstance(g, collections.abc.Iterable))
print(isinstance(h, collections.abc.Iterable))
print(isinstance(a, collections.abc.Iterator))
print(isinstance(b, collections.abc.Iterator))
print(isinstance(c, collections.abc.Iterator))
print(isinstance(d, collections.abc.Iterator))
print(isinstance(e, collections.abc.Iterator))
print(isinstance
