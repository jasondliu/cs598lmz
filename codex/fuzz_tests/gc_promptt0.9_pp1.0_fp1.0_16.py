import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class C:
    pass
o = C()
o.x = C()
o.y = [C()]
ry = weakref.ref(o.y)
o.z = {'a':C()}
rd = weakref.ref(o.z)
wr = weakref.ref(o)
del o
gc.collect()
print rd(), ry(), wr()
