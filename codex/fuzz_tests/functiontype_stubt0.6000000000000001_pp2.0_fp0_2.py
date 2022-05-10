from types import FunctionType
a = (x for x in [1])
b = [1,2]
c = set([1,2,3])
d = {'a':1}
e = FunctionType(lambda:None, globals())
print(type(a), type(b), type(c), type(d), type(e))

# iterable
print(hasattr(a, '__iter__'))
print(hasattr(b, '__iter__'))
print(hasattr(c, '__iter__'))
print(hasattr(d, '__iter__'))
print(hasattr(e, '__iter__'))

# iterator
print(hasattr(a, '__next__'))
print(hasattr(b, '__next__'))
print(hasattr(c, '__next__'))
print(hasattr(d, '__next__'))
print(hasattr(e, '__next__'))

# iter
print(isinstance(a, abc.Iterable))
print(isinstance(b, abc.Iterable))
print(isinstance(c, abc
