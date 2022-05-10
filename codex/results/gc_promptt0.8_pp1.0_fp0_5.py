import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a bunch of objects all referring to each other.
# Collecting them all will cause the repr() of the objects to be called.
# If that happens to crash, the test fails.  If one of the items is a dict
# (as it most likely is on CPython), and the dict implementation crashes,
# there's no guarantee that the objects will be collected and the repr() will
# be called.  To fix this, we use a list containing all objects and weak
# references to them.  This way, it's guaranteed that the objects will be
# collected.  On CPython, reusing the same weakref object is fine.  On PyPy,
# we need to use a fresh weakref to each object, because the old one is
# cleared when the object is collected.
objs = []
refs = []
for i in range(10):
    objs += [
        [], {}, (), set(), frozenset(), object(), type("", (), {}),
        # some additional classes
        new.classobj("", (object,), {}),
        type("", (object,), {}),
    ]

