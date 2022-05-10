import weakref
# Test weakref.ref()
from test import support
class Number:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return '<Number %s>' % self.n
class Subclass(Number):
    pass
class Broke(Number):
    def __hash__(self):
        raise RuntimeError
    def __eq__(self, other):
        raise RuntimeError
class Destroyed:
    destroyed = 0
    def __init__(self, name):
        self.name = name
    def __del__(self):
        Destroyed.destroyed += 1
        if Destroyed.destroyed > 3:
            raise Exception('too many __del__ methods called')

a = Destroyed('a')
aref = weakref.ref(a)

# Test basic constructor trapping
class Foo:
    pass
f = Foo()
rf = weakref.ref(f)
del f
assert rf() is None
rf = weakref.ref(Foo())
assert rf() is None
r = weakref.ref(f
