import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class C(object):
    pass

a = C()
b = C()
a.b = b
b.a = a
b.b = b
#
del a
del b
gc.collect()

# Test weakrefs
def f():
    a = C()
    b = C()
    a.b = b
    b.a = a
    b.b = b
    a.w = weakref.ref(a)
    b.w = weakref.ref(b)
    b.aw = weakref.ref(a)
    b.bw = weakref.ref(b)
    a.aw = weakref.ref(a)
    a.bw = weakref.ref(b)
    #
    del a
    del b
    gc.collect()

f()
f()
f()
gc.collect()
gc.collect()

class X(object):
    pass

gc.collect()

# The following line fails when Python is compiled with
# --without-pymalloc.
# See http
