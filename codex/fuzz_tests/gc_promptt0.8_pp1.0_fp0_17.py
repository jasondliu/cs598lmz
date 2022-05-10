import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() while collecting up a chain of weakrefs.
class A(object):
    pass

a = A()
w1 = weakref.ref(a)
a.a = a
a.b = a.a
a.b.c = a.b
a.b.c.d = a.b.c
a.b.c.d.e = a.b.c.d
a.b.c.d.e.f = a.b.c.d.e

new = gc.collect()
print new, gc.garbage

# Issue #2908
import textwrap
textwrap.wrap(" ", 10, break_long_words=True)
