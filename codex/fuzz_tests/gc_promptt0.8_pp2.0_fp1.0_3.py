import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with collectable objects.
w = weakref.ref(gc.collect())
del w
gc.collect()

# Verify weakref callbacks.
if verbose:
    print("Verifying weakref callbacks...")
cb = weakref.ref(
    lambda : None,
    lambda w: callback_check.append(w)
    )
gc.collect()
if not callback_check:
    raise TestFailed("Weakref callback not called")
callback_check = []

if verbose:
    print("Verifying weakref callbacks for cyclic trash...")

class X:
    pass

a = X()
a.b = X()
a.c = a.b
a.d = weakref.ref(a)
del a.d

# This makes the cyclic trash into a cycle involving a dict,
# rather than a straight chain.  This is a little more interesting.
x = {}
x["a"] = a
a = x

# XXX:  This turns out to be a red herring.  The new collection
# algorithm notices no difference in
