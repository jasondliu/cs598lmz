import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without a callback
class A:
    pass
a = A()
weakref.ref(a)
del a
gc.collect()
# test weakref callback
class B:
    pass
b = B()
weakref.ref(b, lambda w: print("callback"))
del b
gc.collect()
# test a weakref callback that causes a gc collect
class C:
    pass
c = C()
weakref.ref(c, lambda w: gc.collect())
del c
gc.collect()
# test a weakref callback that causes a gc collect
class D:
    pass
d = D()
weakref.ref(d, lambda w: gc.collect())
del d
gc.collect()
# test a weakref callback that causes a gc collect
class E:
    pass
e = E()
weakref.ref(e, lambda w: gc.collect())
del e
gc.collect()
# test a weakref callback that causes a gc collect
class F:
    pass
f = F()
weakref.ref(f, lambda w
