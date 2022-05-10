import weakref
# Test weakref.ref()
import gc
import sys

class A:
    pass

class B(A):
    pass

class C(A):
    pass

a = A()
b = B()
c = C()

wr = weakref.ref(a)
assert wr() is a
assert wr.__class__ is weakref.ref
assert wr.__eq__(wr) is NotImplemented
assert wr.__ne__(wr) is NotImplemented
assert wr.__hash__() == hash(a)
assert repr(wr) == "<weakref at %#x; to 'A' at %#x>" % (id(wr), id(a))

wr = weakref.ref(b)
assert wr() is b
assert wr.__class__ is weakref.ref
assert wr.__eq__(wr) is NotImplemented
assert wr.__ne__(wr) is NotImplemented
assert wr.__hash__() == hash(b)
