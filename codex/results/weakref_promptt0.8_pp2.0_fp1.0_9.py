import weakref
# Test weakref.ref(Foo)() works correctly.
#
# Also test __del__ method for weakref.
# Note that this may not be tested by this test:
# - If a weakref is the last reference to an object, and the weakref's
#   __del__ method is called by the garbage collector, the object will be
#   deleted before __del__ is called.
# - If a weakref is the last reference to an object, and the weakref's
#   __del__ method is called by the garbage collector, the object will
#   not be deleted twice.

class Foo:
    def __init__(self, x):
        self.x = x
        self.called = False
        self.wr = weakref.ref(self, self.callback)

    def callback(self, wr):
        self.called = True
        self.wr = wr
        self.x = 42

f = Foo(5)
f.x = 6
f.x = 7
assert f.wr().x == 7
f.x = 8
assert f.wr().x == 8
del f.x
