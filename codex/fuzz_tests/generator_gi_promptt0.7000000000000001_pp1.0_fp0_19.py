gi = (i for i in ())
# Test gi.gi_code.co_varnames

# Test that gi.gi_frame is always None

class C:
    def __iter__(self):
        return self

    def __next__(self):
        return 0

class D(C):
    def __iter__(self):
        return iter(super())

# Test that an iterator that returns itself is valid
i = iter(C())
assert i is i.__iter__()
# Test that an iterator that returns a base class iterator is valid
i = iter(D())
assert i is i.__iter__()

class E:
    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

assert list(E()) == []

# Test that generators implement the iterator protocol

def g():
    yield 1
    yield 2

g = g()
assert g.__iter__() is g

# Test that generators are proper iterators

def g():
    yield 1

i = g()
assert i is iter(i)

# Test that StopIter
