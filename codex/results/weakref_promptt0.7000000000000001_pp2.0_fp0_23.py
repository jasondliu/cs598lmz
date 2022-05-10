import weakref
# Test weakref.ref with callbacks
import _weakref
import gc

def f():
    pass

class C:
    def __init__(self):
        self.callback_args = None
        self.callback_called = False
    def mycallback(self, arg):
        self.callback_called = True
        self.callback_args = arg

class D(C):
    def mycallback(self, arg):
        C.mycallback(self, arg)
        raise KeyError

class FinalizeTest(unittest.TestCase):

    def callback(self, arg):
        self.callback_called = True
        self.callback_args = arg

    def setUp(self):
        self.callback_called = False
        self.callback_args = None

    def test_basic(self):
        o = C()
        wr = weakref.ref(o, o.mycallback)
        self.assertEqual(wr(), o)
        self.assertFalse(o.callback_called)
        self.assertIsNone(o.callback_args)

        del o

