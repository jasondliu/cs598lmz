import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() issue5849

# Test that gc.collect() works basically at all, even if it doesn't
# collect much.
gc.collect()


def f():
    pass


# A function attached to a function.
f.attr = f
wr = weakref.ref(f)
del f
gc.collect()
assert wr()


class C(object):

    attr = None

    def __init__(self, a):
        self.a = a


# A function attached to an instance.
c = C(f)
wr = weakref.ref(c)
del c
gc.collect()
assert wr()


# A function attached to a class.
C.attr = f
wr = weakref.ref(C)
del C
gc.collect()
assert wr()


def g():
    pass


# A cycle involving functions.
f.attr = g
g.attr = f
wr = weakref.ref(f)
del f, g
gc.collect()
assert wr()

# Make sure all of the above cases are also true when there
