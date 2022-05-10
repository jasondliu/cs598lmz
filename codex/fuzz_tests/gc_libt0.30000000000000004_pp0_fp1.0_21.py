import gc, weakref

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)

print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(o is o2)

del o2

print(gc.collect())

print(r2())

print(gc.collect())

print(r2())

print(gc.collect())

print(r2())

del o

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

print(r())

print(gc.collect())

