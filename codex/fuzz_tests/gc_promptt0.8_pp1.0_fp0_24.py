import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect flags


class C:
    pass


class E:
    pass


class C1(C):
    pass


class C2(C):
    pass


class C3(C):
    pass


c = C()
e = E()
e1 = C1()
e2 = C2()
e3 = C3()
e4 = C1()
e5 = C2()

w = weakref.ref(c)
k = weakref.ref(e)
for x in (e1, e2, e3, e4, e5):
    w = weakref.ref(x)
del c, e, e1, e2, e3, e4, e5
with gc.collect(2) as res:
    print(res & gc.DEBUG_SAVEALL)
with gc.collect(0) as res:
    print(res & gc.DEBUG_SAVEALL)
with gc.collect(1) as res:
    print(res & gc.DEBUG_SAVEALL)
gc.set_debug
