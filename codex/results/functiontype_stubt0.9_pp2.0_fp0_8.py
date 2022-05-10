from types import FunctionType
a = (x for x in [1])
b = a
b.__length_hint__ = FunctionType(lambda self: 0.0, b, type(b))
list(b)
s = set()
s.add(a)
s.__len__ = FunctionType(lambda self: 0.0, s, type(s))
list(s)[0].__next__()
</code>

