import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
gc.collect()
print(r)
print(r())
