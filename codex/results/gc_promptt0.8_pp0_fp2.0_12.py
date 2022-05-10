import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test:
    pass

a = Test()
# a is now a reference to a Test() object.
# Remove references a and b
# gc.collect() waits for the next generation
a = None
# This is necessary because the code under test is guarded by the
# global
# _PyThreadState_Current->gilstate_counter != 0
# which causes the code being tested to be skipped.
# The next generation has not started yet.
gc.collect()
# Now the object is gone.
```

```
# Check that we correctly detect fatal errors
import weakref

def f():
    return weakref.ref(weakref.ref(None))

# f() returns a weakref to a weakref to None.  The weakref to None
# gets deallocated immediately because there is no strong reference
# to it.  The weakref object itself is collected only at the next
# collection pass.  This tests that we correctly detect fatal errors
# when finalizing "resurrected" objects.

# Create a weakref to the function f().  This is necessary because
#
