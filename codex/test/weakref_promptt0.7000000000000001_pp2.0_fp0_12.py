import weakref
# Test weakref.ref.
#
# This test must be run with the -uall option.

import gc

#
# Check basic operation of a weak reference.
#

class A:
    pass

a = A()
r = weakref.ref(a)
assert r() is a
del a
assert gc.collect() == 1
assert r() is None

#
# Check basic operation of a proxy.
#

class B:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return "B(%r)" % self.arg

b = B(1)
r = weakref.proxy(b)
assert r.arg == b.arg == 1
b.arg = 2
assert r.arg == b.arg == 2
del b
gc.collect()
try:
    r.arg
except ReferenceError:
    pass
