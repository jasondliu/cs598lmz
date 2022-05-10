import weakref
# Test weakref.ref() and weakref.proxies

import unittest
import pickle
from weakref import ref, proxy, print_weakrefs, getweakrefcount, getweakrefs
from gc import collect

class C(object):
    pass

class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

# Test single references
class WeakrefTest(unittest.TestCase):

    def setUp(self):
        self.o = C()
        self.r = ref(self.o)

    def test_exception(self):
        # Test for exception-raising behaviour.
        self.assertRaises(TypeError, ref, 1, 2)
        self.assertRaises(TypeError, ref, C(), C())
        self.assertRaises(TypeError, ref, D())
        self.assertRaises(TypeError, proxy, D())

