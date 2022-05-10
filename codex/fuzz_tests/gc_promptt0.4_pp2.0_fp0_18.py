import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs

class A:
    pass

class B:
    pass

a = A()
b = B()
a.b = b
b.a = a

# create a cycle
a.b.a.b = b

# create a weakref cycle
w = weakref.ref(a)
b.w = w

# create a weakref to a function
def f():
    pass

w2 = weakref.ref(f)

del a, b, w, w2, f

# collect everything
gc.collect()

# check that the weakrefs are gone
print gc.get_referrers(B)
print gc.get_referrers(A)
print gc.get_referrers(f)
