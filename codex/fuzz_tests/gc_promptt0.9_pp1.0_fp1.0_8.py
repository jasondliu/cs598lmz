import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, weakref.ReferenceType.__init__ and __del__.

class X(object):
    def __init__(self):
        self.wref = weakref.ref(self, self.callback)
        gc.collect()
        assert not self.wref()

    def callback(self, wr):
        pass

    def __del__(self):
        pass

# Check that the callback is called just before __del__
class Foo(object):
    def __init__(self):
        self.wref = weakref.ref(self, self.callback)
        assert self.wref()
        del self
        gc.collect()

    def callback(self, wr):
        assert wr()

    def __del__(self):
        pass


class Test:
    ok = True
    def _destructor(self, arg):
        assert Test.ok
        self.ok = False
        assert isinstance(arg, Test)

    def __init__(self):
        self.ref = weakref.ref(self, self._destructor)

    def
