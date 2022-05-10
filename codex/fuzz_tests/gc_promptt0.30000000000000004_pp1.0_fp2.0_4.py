import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback
# that raises an exception.

class A:
    pass

def callback(wr):
    raise Exception

a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()

# Check that the exception is not swallowed
try:
    gc.collect()
except Exception:
    pass
else:
    raise TestFailed, "expected exception"

# Check that the callback is not called again
try:
    gc.collect()
except Exception:
    raise TestFailed, "unexpected exception"

# Check that the exception is not swallowed
try:
    gc.collect()
except Exception:
    pass
else:
    raise TestFailed, "expected exception"
