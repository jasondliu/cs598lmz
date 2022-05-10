import gc, weakref
from . import util

#-------------------------------------------------------------------------------
class Test_01_Basic(util.TestCase):

    def test_00_basic(self):
        a = weakref.WeakSet()
        self.assertEqual(len(a), 0)
        self.assertEqual(list(a), [])
        a.add(1)
        self.assertEqual(len(a), 1)
        self.assertEqual(list(a), [1])
        a.add(1)
        self.assertEqual(len(a), 1)
        self.assertEqual(list(a), [1])
        a.add(2)
        self.assertEqual(len(a), 2)
        self.assertEqual(list(a), [1, 2])
        a.add(2)
        self.assertEqual(len(a), 2)
        self.assertEqual(list(a), [1, 2])
        a.add(3)
        self.assertEqual(len(a), 3)
        self.assertEqual(list
