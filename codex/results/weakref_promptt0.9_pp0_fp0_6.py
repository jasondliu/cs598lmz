import weakref
# Test weakref.ref(a) is weakref.ref(b) if a is b
class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)

a = A(1)
assert weakref.ref(a) is weakref.ref(a)
assert not (weakref.ref(a) == weakref.ref(a))

# Subclasses of weakref.ref shouldn't directly implement a __hash__
# method, but instead should inherit the default one from weakref.ref
# (if defined).  The hash of a weakref instance shouldn't change.  It
# should be derived from the object's identity, not its contents.

r = weakref.ref(a)
r2 = weakref.ref(a)
# Both references point to the same object, so they're identical.
assert r == r2
# A hash function is required for r to have a truth value
assert r

a2 = A(2)
# If a is b and weakref.ref(a) is
