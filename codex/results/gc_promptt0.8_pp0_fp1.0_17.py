import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref callbacks.


class A:
    def __del__(self):
        seen.append(1)


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(A):
    pass


base = A()
b1 = B()
b2 = B()
c = C()
d = D()
e = E()
l = [base, b1, b2, c, d, e]
base.l = l[:]
b1.l = l[:]
b2.l = l[:]
c.l = l[:]
d.l = l[:]
e.l = l[:]
del l
seen = []


def callback(ref):
    seen.append(ref)


def ref(obj):
    s = str(obj)
    return weakref.ref(obj, callback)


ref(base)
ref(b1)
ref(b2)
ref(c)
ref(d)
ref(e)
del base
