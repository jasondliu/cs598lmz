import gc, weakref

class C:
    pass

c = C()
r = weakref.ref(c)

print(r())

c = None

gc.collect()

print(r())

class C:
    pass

c = C()
r = weakref.ref(c)

print(r())

c = None

gc.collect()

print(r())
