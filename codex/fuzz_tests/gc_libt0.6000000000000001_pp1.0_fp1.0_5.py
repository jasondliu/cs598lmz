import gc, weakref

from test import mapping_tests
from test import string_tests
from test import seq_tests

class Object:
    pass

class WeakrefTest(unittest.TestCase):

    def test_basic(self):
        o = Object()
        wr = weakref.ref(o)
        self.assert_(wr() is o)
        del o
        self.assert_(wr() is None)

    def test_callbacks(self):
        # Make sure calling a weakref with a dead referent runs the callback
        # and doesn't raise an exception
        callback_ran = []
        def callback(wr):
            self.assert_(wr() is None)
            callback_ran.append(True)
        o = Object()
        wr = weakref.ref(o, callback)
        del o
        gc.collect()
        self.assert_(callback_ran)
        self.assertRaises(TypeError, wr)

    def test_callbacks_cycle(self):
        # Issue #19276: check that a weakref callback doesn't create a cycle
        # with
