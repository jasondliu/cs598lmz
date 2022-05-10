import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, C, D):
    pass

def f():
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    l = [a, b, c, d, e]
    del a, b, c, d, e
    return l

l = f()
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect
