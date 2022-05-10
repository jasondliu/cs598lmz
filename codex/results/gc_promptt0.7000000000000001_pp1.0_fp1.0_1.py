import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback, and with a weakref whose
# target has a __del__() method.

# First, try it with an object that has a __del__() method.

class TestObject(object):
    def __del__(self):
        pass

# This test is a bit different from the others, because it's hard to
# know if the __del__ method will be called.  We know the object is
# dead, but we can't be sure when the __del__ method will be called.
# So, we just try to make sure that the callback is called, and that
# __del__ is called after the callback.

# First, the callback is called.

class TestCase(unittest.TestCase):

    def test_callback_called(self):
        # The callback is invoked with a single argument, the weakref
        # object.  We check that the weakref object refers to the
        # original object.  We then check that del'ing the weakref
        # object does not invoke the callback.
        global callback_called
        callback_called = False

