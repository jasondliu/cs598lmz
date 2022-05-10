import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The current implementation of gc.collect() doesn't actually
# collect anything.  This test is here to make sure it doesn't
# crash or loop.

def f(x):
    print x
    gc.collect()

f("collecting")

# Test gc.get_referents()
#
# This is a very weak test.  It doesn't really check that
# get_referents() does the right thing, but it at least runs
# it on a variety of object types without crashing.

def f(x):
    gc.get_referents(x)

for x in (None,
          1,
          1.0,
          1L,
          1+2j,
          "",
          [],
          (),
          {},
          f,
          weakref.ref(f),
          unittest,
          gc,
          gc.get_referents,
          gc.DEBUG_COLLECTABLE):
    f(x)

# Test gc.get_referrers()
