import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
ref = weakref.ref(gc.collect)
del gc.collect
gc.collect()
assert ref() is None

# Issue #7209: test that a weak reference to a callable can be
# collected
class A:
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback()

def callback():
    print("called back")

a = A(callback)
a_ref = weakref.ref(a)
del a
gc.collect()
assert a_ref() is None

# Issue #7209: test that a weak reference to a callable can be
# collected, even if the callable is a bound method
def callback(self):
    print("called back")

a = A(callback)
a_ref = weakref.ref(a)
del a
gc.collect()
assert a_ref() is None

# Issue #7209: test that a weak reference to a callable can be
# collected, even if the callable is a static method
def callback():

