import weakref
# Test weakref.ref

import gc
import weakref

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c

c2 = C()
r2 = weakref.ref(c2)
assert r2() is c2

c = None
assert r() is None
assert gc.collect() == 0

del r
assert gc.collect() == 0

del r2
assert gc.collect() == 1

assert weakref.getweakrefcount(c2) == 0
assert weakref.getweakrefs(c2) == []


# Test weakref.proxy

import gc
import weakref

class C:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return '<C self=%s arg=%s>' % (id(self), self.arg)

c = C(1)
p = weakref.proxy(c)

assert repr(p) == '<C self=%s arg=
