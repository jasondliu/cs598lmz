import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

for c in [A, B, C, D, E]:
    print(c, c.__mro__)

# Test weakref
a = A()
b = B()
c = C()
d = D()
e = E()

w = weakref.WeakValueDictionary()
w['a'] = a
w['b'] = b
w['c'] = c
w['d'] = d
w['e'] = e

print(w.data)

del a, b, c, d, e

gc.collect()

print(w.data)

# Test gc.get_referrers()
a = A()
b = B()
c = C()
d = D()
e = E()

w = weakref.WeakValueDictionary()
w['a'] = a
w['
