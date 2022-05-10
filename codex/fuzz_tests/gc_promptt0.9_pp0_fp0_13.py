import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at the end of the body

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

x = D()
x.a = A()
x.b = B()
x.c = C()

# weakrefs
x.weak_a = weakref.ref(x.a)
x.weak_b = weakref.ref(x.b)
x.weak_c = weakref.ref(x.c)

print("ok")

gc.collect()

print("x.a=", dir(x.a))
print("x.b=", dir(x.b))
print("x.c=", dir(x.c))
