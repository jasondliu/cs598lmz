import weakref
# Test weakref.ref().

class C(object):
    def method(self):
        return id(self)
    def __eq__(self, other):
        return self is other
    def __ne__(self, other):
        return self is not other

def check(r, live, broken=False):
    if live:
        assert r() is not None
        assert type(r()) is C
        assert r() == c
    else:
        if broken:
            assert r() is None
        else:
            try:
                r()
            except ReferenceError:
                pass
            else:
                assert 0, "shouldn't be able to dereference dead ref"

c = C()
r1 = weakref.ref(c)
check(r1, 1)

# Check the basic get() method
assert live_refcount(r1) == 1
assert r1() is c

# Check the weakref.ref constructor
r2 = weakref.ref(r1())
check(r2, 1)

# Check the proxy constructor
def function(x):
   
