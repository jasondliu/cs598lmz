import gc, weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r() is o

del o
gc.collect()
print r() is None
</code>

