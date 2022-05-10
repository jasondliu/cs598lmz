import weakref
# Test weakref.ref; this is an abstract class, so we have to create a
# subclass.
import unittest
from test import test_support
from weakref import ref

class C(object):
    pass

class D(object):
    pass

class AbstractGeneralTest:
    # test weakref.ref; this is an abstract class, so we have to create a
    # subclass so we can instantiate it.

    def test_basic(self):
        o = C()
        p = ref(o)
        self.assertTrue(p() is o)

    def test_callback_gets_correct_argument(self):
        def callback(arg):
            callback.x = arg
        o = C()
        p = ref(o, callback)
        self.assertTrue(callback.x is o)
        o2 = C()
        p2 = ref(o2, callback)
        self.assertTrue(callback.x is o2)

