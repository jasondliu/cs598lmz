import weakref
# Test weakref.ref() and weakref.proxy()
#
# The following test ensures that weak references to an object and a
# weak proxy to the object are created successfully, and that the proxy
# and the weak reference use the same hash value.
#
# Both the proxy and the weak reference should be hashable, and
# weakref.getweakrefcount() should return 2.

import sys
import weakref
import unittest

class Hashable(object):
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return hash(self.value)
    def __eq__(self, other):
        return self.value == other.value

class TestWeakRef(unittest.TestCase):
    def test_ref(self):
        h = Hashable(42)
        r = weakref.ref(h)
        p = weakref.proxy(h)
        self.assertEqual(hash(r), hash(p))
        self.assertEqual(r(), p)
        self.assertEqual(r(), h)
       
