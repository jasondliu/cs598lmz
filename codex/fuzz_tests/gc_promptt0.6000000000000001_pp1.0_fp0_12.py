import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.collect(2)

class C:
    pass

class D:
    pass

x = C()
x.a = x
y = C()
y.a = y
z = C()
z.a = z

c = weakref.ref(x)
d = weakref.ref(y)
e = weakref.ref(z)

del x, y, z
gc.collect()
gc.collect(2)

print(c())
print(d())
print(e())

print(gc.garbage)
