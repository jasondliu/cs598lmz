import weakref
# Test weakref.ref for cyclic garbage
import gc

#
# Evaluate special cases.
#


def ref(ob):
    return weakref.ref(ob)


def GetObject(wr):
    return wr()


r = ref(None)
assert GetObject(r) is None
