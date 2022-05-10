from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = {'a': 1, 'b': 2}
d = 'abc'
e = FunctionType(lambda: None, {}, '', (), ())
f = object()

print(type(a), type(b), type(c), type(d), type(e), type(f))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))
print(isinstance(d, Iterator))
print(isinstance(e, Iterator))
print(isinstance(f, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(e, Iterable))
print(isinstance(f, Iterable))

print(isinstance(a, Iterator) and isinstance(a, Iterable))
print(isinstance(b, Iterator) and isinstance(b, Iterable))

