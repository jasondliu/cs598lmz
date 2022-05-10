import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()

class A:
    pass

class B:
    pass

a = A()
gc.collectable(a)
del a
#gc.collect()
print

b = B()
gc.collectable(b)
b = 7
print gc.collectable(b)
print

# Test reference leak detection

class C:
    pass

c = C()
gc.collectable(c)
c.foo = c
del c
gc.collect()
print

class D:
    pass


def f():
    d = D()
    gc.collectable(d)
    return d

e = f()
del e
#gc.collect()
print

# Test gc_referrers()

class E:
    pass

e1 = E()
e2 = E()
e1.foo = e2
e2.foo = e1

print gc.get_referrers(e1)
print gc.get_referrers(e2)
#print gc.get_refer
