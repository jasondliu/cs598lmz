import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs to objects with finalizers

# This test must be run with the -l option to regrtest.

import gc

class Foo:
    def __init__(self, i):
        self.i = i
    def __del__(self):
        global finalizer_called
        finalizer_called = self.i

def f():
    global x
    global finalizer_called
    global y
    for i in range(10):
        x = Foo(i)
        y = weakref.ref(x)
        x.y = y
        del x
        gc.collect()
        if finalizer_called is not None:
            break
    else:
        print("finalizer never called")

# Make sure the test doesn't run in parallel with other tests
# (e.g. test_weakref.py).
gc.disable()

finalizer_called = None
x = None
y = None
f()
if finalizer_called not in range(10):
    print("finalizer called with wrong argument: %r" %
