import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test other features of weakref.WeakKeyDictionary

import unittest
from test import test_support

# Test weakref.ref(object)
class Dummy:
    pass

def callback(dummy):
    raise SystemError

def test_basic():
    # Test basic reference behaviour
    d = Dummy()
    p = weakref.ref(d)
    q = weakref.ref(d)
    assert p() is d
    assert q() is d
    assert p is not q
    assert p() is q()

    # Test hash values
    import operator
    assert hash(p) == hash(q)
    assert hash(p) == hash(p)
    assert hash(p) == hash(d)
    assert hash(p) == hash(weakref.ref(d))

    # Test equality
    assert p == q
