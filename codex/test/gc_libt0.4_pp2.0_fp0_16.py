import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)

print(r() is None)

del o
print(r() is None)

gc.collect()
print(r() is None)
