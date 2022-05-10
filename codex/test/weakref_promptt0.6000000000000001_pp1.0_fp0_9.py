import weakref
# Test weakref.ref() with a custom __hash__ method.
import gc

class C:
    def __hash__(self):
        return 0x1234


class D:
    def __hash__(self):
        return 0x5678


class E:
    def __hash__(self):
        return 0x9abc

# Create C, D and E instances, and verify that they are different objects.
# Otherwise this test would be meaningless.
c = C()
d = D()
e = E()
assert c is not d
assert d is not e
assert e is not c
# Create weak references to the objects.
c_ref = weakref.ref(c)
d_ref = weakref.ref(d)
e_ref = weakref.ref(e)
# Verify that the weak references are different.
assert c_ref is not d_ref
assert d_ref is not e_ref
assert e_ref is not c_ref
# Delete c, and verify that it gets cleared from the weak references.
del c
gc.collect()
assert c_ref() is None

