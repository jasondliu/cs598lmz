import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)

o2 = C()
r2 = weakref.ref(o2)

print(r2() is o2)

o = None
gc.collect()

print(r())
print(r() is o)

print(r2() is o2)
