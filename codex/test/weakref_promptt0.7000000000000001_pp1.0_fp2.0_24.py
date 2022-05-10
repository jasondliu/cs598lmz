import weakref
# Test weakref.ref function on a class instance

class C:
    def __init__(self, x=0):
        self.x = x

    def __repr__(self):
        return "C(%d)" % self.x

c = C()
r = weakref.ref(c)
assert r() is c
assert r().x == 0
c.x = 42
assert r().x == 42

d = C(1729)
r2 = weakref.ref(d)
assert r2() is d
assert r2().x == 1729
del d
assert r2() is None
# Test weakref.ref function on a builtin

class Foo:
    def __init__(self, l):
        self.l = l
    def __del__(self):
        self.l.append(1)

l = []
f = Foo(l)
r = weakref.ref(f)
assert r() is f
del f
assert r() is None
assert l == [1]
# Test weakref.ref function on a builtin method
import weak
