import weakref
# Test weakref.ref
def f():
    return 42

class C:
    pass

o = C()
r = weakref.ref(o)
print r() is o
r = weakref.ref(f)
print r()() == 42

# Test weakref.proxy
p = weakref.proxy(o)
print p is o
p = weakref.proxy(f)
print p() == 42

# Make sure that proxy pass through special methods
class D(object):
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __hash__(self):
        return self.value
    def __repr__(self):
        return "D(%r)" % self.value

thing = D(5)
print thing == thing, thing == D(5), thing == D(6)
print repr(thing), repr(weakref.proxy(thing))
print len(set([thing, weakref.proxy(thing)]))

# Test weakref.getweakref
