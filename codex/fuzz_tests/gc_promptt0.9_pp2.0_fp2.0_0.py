import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on some nice example cases.


class C:

    def __init__(self):
        self.x = 1

    def __del__(self):
        global del_calls
        del_calls += 1


ref_calls = 0


def ref(n):
    global ref_calls
    ref_calls += 1
    return id(n)


# Create and collect some open ended loops.
del_calls = 0
c1 = C()
c2 = C()
c1.next = c2
c2.next = c1
weakref.ref(c1, ref)
weakref.ref(c2, ref)
r1 = weakref.ref(c1)
r2 = weakref.ref(c2)
del c1
del c2
gc.collect()
# If the next line causes a crash, uncomment the previous
# line.  An even earlier version of this test used a weakref
# to the class C instead of an instance.  It was removed from
# the test when the corresponding line in PyWeakref_ClearRef
