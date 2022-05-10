import weakref
# Test weakref.ref() and weakref.proxy()
import _weakref
from test.support import TestFailed
from test.test_weakref import (
    getweakrefcount, getweakrefs,
    MyBase, MyObj, MyDerived, MyList, make_callback, MyException
)
# To test weakref.finalize()
import gc
from test.support import run_unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.instances = []

    def tearDown(self):
        for inst in self.instances:
            del inst

    def callback(*args):
        pass

class BasicTestCase(BaseTestCase):

    def test_basic(self):
        a = MyObj()
        a.callback = make_callback('a')
        b = MyObj()
        b.callback = make_callback('b')
        self.instances = a, b
        r1 = weakref.ref(a)
        r2 = weakref.ref(b)
        self.assertEqual(getweak
