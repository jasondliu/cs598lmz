fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_yieldfrom = gi

try:
    fn()
except StopIteration:
    pass


# Test __await__()
class A:
    def __await__(self):
        yield 1
        yield 2


a = A()
g = a.__await__()
assert next(g) == 1
assert list(g) == [2]


# Test __aiter__()
class A:
    def __aiter__(self):
        return self

    def __anext__(self):
        return 1


a = A()
g = a.__aiter__()
assert next(g) == 1


# Test __aenter__() and __aexit__()
class A:
    def __aenter__(self):
        return self

    def __aexit__(self, *args):
        pass


a = A()
with a as b:
    assert b is a
