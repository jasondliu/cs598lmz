import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
def f():
    return gc.collect()

f()
# Test gc.get_referents
a = []
def f():
    return gc.get_referents(a)
def g():
    return a

g() is f()
# Test gc.get_objects
def f(g, *args):
    n = g(*args)
    if n is None:
        return
    print g.__name__
    for x in gc.get_objects():
        if x is gc.garbage[n]:
            print "Found at", n
            break
        n = n+1
    else:
        print "Not found"

def g():
    l = [1,2,3]
    a = l[2:2]
    if a is not []:
        raise TestFailed, "gc.get_objects blows"

f(g)
# Repr of weakrefs
# getnewargs should not blow up!
w = weakref.ref(lambda : None)
repr(w)
#
