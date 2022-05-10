import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
def f():
    s = "abcd"
    l = [1, 2, 3]
    t = (1, 2, 3)
    d = {1:1, 2:2}
    c = complex(1, 0)
    s2 = s + "efg"
    s2 = s + "efg"
    s = None
    l = None
    t = None
    d = None
    c = None
    s2 = None
    gc.collect()
    assert gc.collect() == 0

f()

class X:
    pass

# Test gc.get_referents
def f():
    x = X()
    y = weakref.ref(x)
    x.a = 1
    x.b = 2
    x.c = 3
    x.d = 4
    x.e = 5
    x.f = 6
    x.g = 7
    x.h = 8
    x.i = 9
    x.j = 10
    x.k = 11
    x.l =
