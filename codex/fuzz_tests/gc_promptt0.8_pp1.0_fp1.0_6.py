import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in the presence of weakrefs after objects have been
# finalized.
#
# The point of the test is to show that collect() works with weakrefs
# in lists, as opposed to crashing.

def callback(wr, list, n):
    list.append(n)

def main():
    # Create a list of lists, each with a callback creating a weak
    # reference from its list to another list.  The inner lists are
    # explicitly kept alive to make sure their callbacks don't get
    # collected.
    innerlists = []
    for i in range(100):
        w = []
        innerlists.append(w)
        getattr(w, 'append')
        for j in range(100):
            w.append(weakref.ref(w, callback, [w, j]))
    assert len(innerlists) == 100
    for i in range(100):
        assert len(innerlists[i]) == 100
    del innerlists[:]
    gc.collect()
    # Now the inner lists will disappear, triggering the callbacks,
    # which
