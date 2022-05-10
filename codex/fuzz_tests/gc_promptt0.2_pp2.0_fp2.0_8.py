import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

class Bar(object):
    pass

def f():
    f1 = Foo()
    f2 = Foo()
    f3 = Foo()
    f4 = Foo()
    f5 = Foo()
    f6 = Foo()
    f7 = Foo()
    f8 = Foo()
    f9 = Foo()
    f10 = Foo()
    f11 = Foo()
    f12 = Foo()
    f13 = Foo()
    f14 = Foo()
    f15 = Foo()
    f16 = Foo()
    f17 = Foo()
    f18 = Foo()
    f19 = Foo()
    f20 = Foo()
    f21 = Foo()
    f22 = Foo()
    f23 = Foo()
    f24 = Foo()
    f25 = Foo()
    f26 = Foo()
    f27 = Foo()
    f28 = Foo()
    f29 = Foo()
    f30 = Foo()
    f31 = Foo()
    f32 = Foo()
    f33 =
