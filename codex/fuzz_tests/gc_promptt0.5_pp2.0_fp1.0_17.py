import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a subclass.
class C(object):
    pass

class D(C):
    pass

o = D()
w = weakref.ref(o)
print(w)

gc.collect()
print(w)

o = None
gc.collect()
print(w)

# Test gc.collect() with a weakref to a subclass.
class C(object):
    pass

class D(C):
    pass

o = D()
w = weakref.ref(o)
print(w)

gc.collect()
print(w)

o = None
gc.collect()
print(w)
