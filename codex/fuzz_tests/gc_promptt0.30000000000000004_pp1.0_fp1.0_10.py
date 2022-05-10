import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
w = weakref.ref(a)
del a
gc.collect()
print(w())

# Test gc.collect() with uncollectable
class B:
    pass

b = B()
b.b = b
w = weakref.ref(b)
del b
gc.collect()
print(w())

# Test gc.collect() with cyclic garbage
class C:
    pass

class D:
    pass

c = C()
d = D()
c.d = d
d.c = c
w = weakref.ref(c)
del c
del d
gc.collect()
print(w())

# Test gc.collect() with uncollectable cyclic garbage
class E:
    pass

class F:
    pass

e = E()
f = F()
e.f = f
f.e = e
w = weakref.ref(e)
del e
del f
gc.collect()
print(w())

# Test gc
