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
print(gc.collect())
print(w())
print(gc.collect())
print(w())

x = None
print(gc.collect())
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

s1 = {x:1}
s2 = {y:1}
s3 = {z:1}
s4 = {a:1}

d1 = {1
