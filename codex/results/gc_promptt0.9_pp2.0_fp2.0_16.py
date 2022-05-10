import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect when a take_ref is pending,
# and test where cyclic references are created during the call to
# gc.collect.
# First create some objects...
# the cycle is a,b,c,d,e,a,f,g,h,a
a = Box()
b = Box()
c = Box()
d = Box()
e = Box()
f = Box()
g = Box()
h = Box()
a.set(b)
b.set(c)
c.set(d)
d.set(e)
e.set(a)
a.set(f)
f.set(g)
g.set(h)
h.set(a)
# Now we have a cycle; each element points to the next one.
# Now we have a2,b2,c2,d2,e2,a2; each element points to the next one.
# This looks a bit like the cycle, but each element "alternates"
a2 = Box()
b2 = Box()
c2 = Box()
d2 = Box()
e2 =
