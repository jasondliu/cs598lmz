import weakref
# Test weakref.ref()

class C:
    def __init__(self, arg=None):
        self.arg = arg
    def __repr__(self):
        return "<C %s>" % (self.arg,)
    def method(self):
        return self.arg

class D(C):
    pass

def test_newstyle(C):
    # Create some instances
    c1 = C(1)
    c2 = C(2)
    c3 = C(3)

    # Create some weak references
    w1 = weakref.ref(c1)
    w2 = weakref.ref(c2)
    w3 = weakref.ref(c3)

    # Check that the weakrefs can be called
    assert w1() is c1
    assert w2() is c2
    assert w3() is c3

    # Check that the weakrefs can be compared
    assert w1 == w1
    assert w1 != w2
    assert w1 != w3
    assert w2 != w1
    assert w2 == w2
   
