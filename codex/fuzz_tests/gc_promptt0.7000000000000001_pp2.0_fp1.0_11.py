import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with cyclic garbage whose only reference is in a global
# variable.
def test_gc_with_global_cycle():
    class A:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "<A %s>" % self.name
    global g
    g = [A("one"), A("two"), A("three")]
    g.append(g)
    g = weakref.ref(g)
    gc.collect()
    assert g() is None, "gc.collect() didn't collect cyclic garbage with only a global reference"

test_gc_with_global_cycle()
