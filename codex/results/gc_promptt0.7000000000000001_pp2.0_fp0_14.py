import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
class C:
    pass

def func(n):
    o = C()
    if n < 10:
        func(n+1)

func(0)

import gc
gc.collect()

 
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

def f(n):
    if n < 10:
        return f(n+1)

def g():
    print "Creating l"
    l = []
    l.append(l)
    print "Setting l =", l
    return l

def h():
    print "Creating l"
    l = []
    l.append(l)
    print "About to return l"
    return weakref.ref(l)

print "Calling f(0)"
x = f(0)
print "Calling g()"
y = g()
print "Calling h()"
z = h()
print "Calling gc.collect()"
gc.collect()
