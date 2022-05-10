import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Collecting `uncollectable` objects
# Simple case when no reference to object
def collect_indirect1():
    global cls3
    cls3 = None
    gc.collect()
    assert gc.collect() == 2

def collect_indirect2():
    global cls4
    cls4 = None
    gc.collect()
    assert gc.collect() == 3 

def test_gc2():
    collect_indirect1()
    collect_indirect2()

# A bit more complex case, when object referenced indirectly while it's being finalised
def test_gc3():
    global lst, cls6
    lst = []
    cls6 = None
    gc.collect()
    assert len(lst) == 1
    assert gc.collect() == 1
    assert len(lst) == 2
    assert gc.collect() == 0

# Same case, for a weakref'able object
target = 42
def test_gc4():
    global ref, cls7
    ref = weakref
