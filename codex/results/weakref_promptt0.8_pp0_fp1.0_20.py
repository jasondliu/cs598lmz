import weakref
# Test weakref.ref()
import __builtin__

class X(object):
    pass

class Y(object):
    def __init__(self):
        self.x = X()
        self.xref = weakref.ref(self.x)
        self.intref = weakref.ref(5)
        self.fnref = weakref.ref(__builtin__.pow)

def test():
    y = Y()
    assert y.xref() is y.x
    assert y.intref() == 5
    assert y.fnref() is __builtin__.pow
    del y.x
    gc.collect()
    assert y.xref() is None
    assert y.intref() == 5
    assert y.fnref() is __builtin__.pow


# This is the same test as above except that we call ref() in the class
# definition.  This means that the reference only goes away if the whole
# class is deallocated, and that requires some special attention.  See
# also extcheck.py.  This test is meant to
