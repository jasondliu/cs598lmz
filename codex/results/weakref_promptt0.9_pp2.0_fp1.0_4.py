import weakref
# Test weakref.ref argument
#
import unittest
class WaitForDel(object):
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback(id(self))
weakref._test()
class C(object):
    pass
w = weakref.ref(C())
x = weakref.WeakValueDictionary(w)
del w
import gc
gc.collect()
class WTest(unittest.TestCase):
    def test_callback(self):
        l = []
        o = WaitForDel(l.append)
        oid = id(o)
        w1 = weakref.ref(o, l.append)
        w2 = weakref.ref(o, l.append)
        del o, w1, w2
        gc.collect()
        self.assertTrue(len(l) == 3)
        self.assertEqual(l[0], oid)
        self.assertEqual(l[1], oid)
        self.assertEqual(l[2],
