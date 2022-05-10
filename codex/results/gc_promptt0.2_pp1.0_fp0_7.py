import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

class Bar:
    pass

def f():
    f = Foo()
    f.b = Bar()
    return f

f1 = f()
f2 = f()
f3 = f()
f4 = f()
f5 = f()
f6 = f()
f7 = f()
f8 = f()
f9 = f()
f10 = f()
f11 = f()
f12 = f()
f13 = f()
f14 = f()
f15 = f()
f16 = f()
f17 = f()
f18 = f()
f19 = f()
f20 = f()
f21 = f()
f22 = f()
f23 = f()
f24 = f()
f25 = f()
f26 = f()
f27 = f()
f28 = f()
f29 = f()
f30 = f()
f31 = f()
f32 = f()
f33 = f()
f34 = f()
f35 = f()
f36 =
