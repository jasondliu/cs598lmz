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

