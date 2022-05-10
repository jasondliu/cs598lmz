import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when objects are in the "uncollectable" state.

def print_state(message, obj):
    print message,
    print 'state:',
    if strongref.getweakrefcount(obj) > 0:
        print 'weakly referenced:', strongref.getweakrefs(obj)
    else:
        print 'not weakly referenced'

def print_referrers(obj):
    for o in gc.get_referrers(obj):
        print repr(o)[:100]

class C:
    pass

# Create an uncollectable object.
c = C()
print_state('c:', c)
# Create a weak reference to the object.
x = weakref.ref(c)
print_state('c:', c)
# Create a cycle containing the object.
c.x = c
print_state('c:', c)
# Create another cycle containing the object.
c.y = c
print_state('c:', c)
# Break the cycle, making the object collectable.
del c.x
print_state
