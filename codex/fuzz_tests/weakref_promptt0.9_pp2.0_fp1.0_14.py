import weakref
# Test weakref.ref
class A(object):
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        return "A(%d)" % self.i

class B(A):
    pass

for factory in [weakref.ref, weakref.WeakKeyDictionary, weakref.WeakValueDictionary]:
    a = A(42)
    w = factory(a)

    assert type(w) is factory
    assert a == w()
    assert w().i == 42

    a = B(1)
    b = B(2)
    w = factory(a)
    assert a == w()
    assert w().i == 1

    # show that WeakKeyDictionary works
    if factory is weakref.WeakKeyDictionary:
        d = w()
        d[b] = 1
        assert d[b] == 1
        assert b not in d
        assert a in d
        # this fails, XXX try to figure out why
        #w = factory(a)
        #assert a in w()

    # show
