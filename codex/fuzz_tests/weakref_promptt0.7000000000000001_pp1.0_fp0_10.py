import weakref
# Test weakref.ref()
from test import test_support

class C:
    def __init__(self):
        self.data = 'spam'

class D(C):
    pass

# Test basic operation

def test_basic():
    o = C()
    wr = weakref.ref(o)
    assert wr() is o
    assert wr.data is o.data
    o.data = 'newvalue'
    assert wr.data == 'newvalue'
    del o
    assert wr() is None

def test_callback():
    # Test that the callback is called when the referent is about to be
    # destroyed
    results = []
    def callback(wr):
        results.append(wr)
    o = C()
    wr = weakref.ref(o, callback)
    assert wr() is o
    del o
    assert wr() is None
    assert results == [wr]

def test_del():
    # Test that weakrefs can be explicitly deleted
    o = C()
    wr = weakref.ref(o)
    assert wr()
