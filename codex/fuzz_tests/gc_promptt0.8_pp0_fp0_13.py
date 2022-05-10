import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before set_threshold()
# No uncollectable objects are created.
gc.collect()
gc.set_threshold(0)
gc.set_threshold(1000)
gc.collect()

# Test gc.get_threshold()
gc.get_threshold()

# Test finalizers
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

# a's __del__() deletes b.
a = A(1)
b = A(2)
a.b = b
b.a = a

def finalize_test(ignored=None):
    if a.b is not b:
        print("finalization corrupted objects", a, b)
    elif b.a is not a:
        print("finalization corrupted objects", a, b)
    else:
        print("finalization didn't corrupt objects", a, b)

a.finalizer = weakref.finalize(a, finalize_test, a)

