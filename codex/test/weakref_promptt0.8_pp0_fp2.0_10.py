import weakref
# Test weakref.ref() with subclass of weakref.ref()

# Create a base class
class Base(object):
    def __init__(self, v):
        self.value = v

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Base) and self.value == other.value

# Create a subclass of weakref.ref()
class MyRef(weakref.ref):
    pass

bases = dict((b.value, b) for b in (Base(i) for i in range(20)))

def test_ref(factory):
    refs = dict((b, factory(b)) for b in bases.values())
    for b, ref in refs.items():
        assert ref() is b
    for b, ref in refs.items():
        del b
    for b, ref in refs.items():
        assert ref() is None

def test_proto():
    proto = Base(10)
