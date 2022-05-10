import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    x = C()
    x.x = x
    return x

gc.collect()
gc.collect()

# Create a cycle with a finalizer
l = []
def finalize(x):
    l.append(x)

c = C()
c.x = c
wr = weakref.ref(c, finalize)

# Create a cycle with a finalizer that raises an exception
# (but the cycle is not in the finalization list)
def finalize_exception(x):
    raise ValueError

c = C()
c.x = c
wr = weakref.ref(c, finalize_exception)

# Create a cycle with a finalizer that raises an exception
# (and the cycle is in the finalization list)
def finalize_exception(x):
    raise ValueError

c = C()
c.x = c
wr = weakref.ref(c, finalize_exception)

import gc
gc.garbage.append(c)

#
