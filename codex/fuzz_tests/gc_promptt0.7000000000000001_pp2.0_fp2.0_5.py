import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakref callback with a reference to the weakref.
def callback(wr, ignored):
    if wr() is not None:
        print("callback called with non-None argument")
        print(wr)
        print(wr())
    else:
        print("callback called with None argument")


def make_callback(i, L):
    return (lambda o: callback(weakref.ref(o), L))


def make_callback_bug(i, L):
    return (lambda o: callback(weakref.ref(o), L))

# This is a test case that used to cause an infinite loop when we were an
# older version of Python.  I've changed it to use lists to avoid having to
# write a metaclass.  It's not clear to me that this is a good test case,
# since we're not actually testing weakrefs to callables.  It does cause
# a segfault in 2.4a0, though.  It should be removed once we're sure we
# don't have the segfault any more.


def test():
    c
