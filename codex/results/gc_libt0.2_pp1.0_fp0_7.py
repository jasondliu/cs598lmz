import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o2)

print(o is o2)

o = None
print(r())

gc.collect()
print(r())

print(r() is None)

print(r() is None)

print(r() is None)
