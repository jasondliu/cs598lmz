import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() works with the following conditions.
#   - objects with weakrefable instances
#   - weak references to objects with a finalizer

class TestWeakrefDestructor:
    def __del__(self):
        pass

class TestWeakrefableDestructor:
    def __del__(self):
        pass
    def __init__(self):
        self.wr = weakref.ref(self)

class TestNonWeakrefableDestructor:
    def __del__(self):
        pass

class TestWeakrefDestructor:
    def __init__(self, obj):
        self.wr = weakref.ref(obj)
    def __del__(self):
        pass

class TestWeakrefableWithFinalizer:
    def __del__(self):
        pass
    def __init__(self):
        self.wr = weakref.ref(self)
        self.td = TestWeakrefDestructor(self)

class TestNonWeakrefableWithFinalizer:
    def __del__(self):
        pass
    def __init
