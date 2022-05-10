import weakref
# Test weakref.ref() on a function.
import sys
import gc
from test.support import run_unittest


class FunctionWeakrefTest(unittest.TestCase):

    def f(self):
        pass

    def test(self):
        f = self.f
        rf = weakref.ref(self.f)
        self.assertEqual(rf(), f)
        f = None
        self.assertEqual(rf(), self.f)

    def test_callback(self):
        f = self.f
        record = []

        def callback(r):
            record.append(r)
        rf = weakref.ref(self.f, callback)

        def del_f():
            del f
        self.assertEqual(rf(), self.f)
        run_with_locale(del_f)
        self.assertIs(rf(), None)
        self.assertEqual(len(record), 1)
        self.assertIs(record[0](), None)
        del rf
        self.assertEqual(len(record), 1)
