import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
class A:
    pass
a = A()

print gc.collectable(a)
del a
print gc.collectable(A)

a = []
b = a
a.append(a)
print gc.collectable(a)
print gc.collectable(b)

a = []
b = a
a.append(a)
print gc.collectable(a)

class A:
    pass
a = A()
b = A()
a.child = b
b.parent = a
print gc.collectable(a)
print gc.collectable(b)

a = []
b = A()
b.child = a
a.append(b)
print gc.collectable(a)
print gc.collectable(b)

a = []
b = A()
b.child = a
a.append(b)
print gc.collectable(a)
print gc.collectable(b)

a = []
b = A()
b.child = a
b.
