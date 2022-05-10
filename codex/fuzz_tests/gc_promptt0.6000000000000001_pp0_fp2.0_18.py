import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weak references
class Foo:
    pass
f = Foo()
def bar():
    f.a = 1
    f.b = 2
    del f.a, f.b
    f.a = 3
    f.b = 4
    del f.a, f.b
    f.a = 5
    f.b = 6
    del f.a, f.b
    f.a = 7
    f.b = 8
    del f.a, f.b
    f.a = 9
    f.b = 10
    del f.a, f.b
    f.a = 11
    f.b = 12
    del f.a, f.b
    f.a = 13
    f.b = 14
    del f.a, f.b
    f.a = 15
    f.b = 16
    del f.a, f.b
    f.a = 17
    f.b = 18
    del f.a, f.b
    f.a = 19
    f.b = 20
    del f.
