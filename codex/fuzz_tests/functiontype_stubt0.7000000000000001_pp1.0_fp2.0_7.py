from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
type(a), type(b)

def f(x): return x
type(f), type(f())

# The reason you can call a generator is that it is an object that implements the iterator protocol
# which means __iter__() and __next__() methods

# Python 2
class M(object):
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def next(self): return self.n

# Python 3
class M(object):
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self): return self.n


# __next__ is called by next
a = M(1)
type(a)
a.__iter__()
a.__next__()
next(a)

# the iterator protocol is used not only by for
it = iter(a)
next(it)
next(it)

# the generator protocol is a subcase of the
