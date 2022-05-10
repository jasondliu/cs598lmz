import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect behavior with cycles and pointers to self
class x(object):
    pass

class weakx(weakref.WeakKeyDictionary):
    pass

a = x()
b = x()
a.ref = b
b.ref = a

def bug256982(x):

    # Test pointer to self
    x.ref = x
    
    # Test cycle with one object
    x.cycle = x
    
    # Test cycle with two objects
    ids = id(x), id(x.ref)
    for i in range(10):
        x = x.ref   # Reassign to different object in cycle
        assert id(x) in ids
        
    # Test cycle with five objects
    l = [x, x.ref, x.cycle, x.cycle.ref, x.cycle.cycle]
    assert len(set(map(id, l))) == 5, l
    
    # We're done creating cycles
    del x, i, l   # Break cycles
    
    # Make sure there aren't any instances of x left around!
    gc
