import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

a = A()
a.b = A()
a.b.a = a
del a
gc.collect()
# Test gc.get_referrers()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

def f():
    a = A()
    a.b = A()
    a.b.a = a

f()

gc.collect()

print(gc.get_referrers(A))
print(gc.get_referrers(a))
print(gc.get_referrers(a.b))
print(gc.get_referrers(a.b.a))
# Test gc.get_referents()
class A:
    pass

a = A()
a.b = A()
a.b.a = a

def f():
    a = A()
    a.b = A()
    a.b.a = a

f()

gc.collect()

print
