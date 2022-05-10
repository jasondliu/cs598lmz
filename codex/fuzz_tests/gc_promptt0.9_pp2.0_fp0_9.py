import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() is not necessary.

# Allocate some memory from the weakrefable pool.  It will select
# sublists non-deterministically, but we just check that all sublists
# have been returned to the reference lists, and that the sublists
# don't contain the same object as one of the sublists that was lent.
# (This last condition cannot be tested deterministically, but we can
# test it probabilistically.)
py.test.skip("debugging, see the weakrefable.c file")
total_nr_of_leaked_references = 0
nr_of_simulations = 1000
for i in range(nr_of_simulations):
    ref = GcRef()
    old_objects = [ref]
    smalls = []
    mediums = []
    larges = []
    for j in range(30):
        ref = GcRef()
        old_objects.append(ref)
        if j == 17:
            p1 = ref
        if j == 26:
            p2 = ref

        weak = ref.allocate()
        # This
