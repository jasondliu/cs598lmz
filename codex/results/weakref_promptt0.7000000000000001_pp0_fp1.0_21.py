import weakref
# Test weakref.ref
from weakref import ref
from weakref import proxy

class C(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

class D(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'D(%r)' % self.x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class E(D):
    pass

class F(D):
    pass

print 'Testing basic ref()'
o = C(1)
r = ref(o)
assert r() is o
o2 = C(2)
r.__init__(o2)
assert r() is o2
del o2
support.gc_collect()
assert r() is None

print 'Testing weakref.proxy()'
o = C(1
