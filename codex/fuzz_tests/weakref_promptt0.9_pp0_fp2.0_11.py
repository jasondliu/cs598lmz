import weakref
# Test weakref.ref on an old-class instance that overrides __eq__
# or __cmp__.
class A:
    def __init__(self, name):
        self.name = name

    def __cmp__(self, other):
        return cmp(self.name, other.name)


class B:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
# Make a test A and B instance.


a = A('a')
b = B('b')
# Create the weakrefs and verify their targets.


ct = weakref.ref(a)
dr = weakref.ref(b)
assert ct() == a
assert dr() == b
# Compare the weakrefs.
assert dr != ct
assert dr == dr
assert ct != dr
assert ct == ct
# Compare a weakref with its target.
assert not (dr == b)
assert dr != b
assert not (dr is b)
assert dr is dr()
assert not (b
