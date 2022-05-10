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

class E:
    pass

for c in [A, B, C, D, E]:
    a = c()
    a = None
    gc.collect()
    print gc.collect()

# Test gc.get_referrers()

a = A()
b = B()
c = C()
d = D()
e = E()

f = [a, b, c, d, e]
g = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}
h = {a: 'a', b: 'b', c: 'c', d: 'd', e: 'e'}

i = [f, g, h]

def j():
    return i

def k():
    return j()

def l():
    return k()

def m():
    return l()

