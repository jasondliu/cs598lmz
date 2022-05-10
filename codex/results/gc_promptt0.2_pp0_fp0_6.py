import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = A()
w = weakref.ref(x)
print(w)
print(w())
del x
print(gc.collect())
print(w)
print(w())

# Test gc.get_referrers()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

x = A()
y = B()
z = C()
a = D()

l1 = [x]
l2 = [y]
l3 = [z]
l4 = [a]

d = {'x': x, 'y': y, 'z': z, 'a': a}

s = set([x, y, z, a])

t = (x, y, z, a)

print(gc.get_referrers(x
