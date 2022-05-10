import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print("in bar")
    a = Foo()
    a.b = Foo()
    a.b.a = a
    wr = weakref.ref(a)
    print(gc.collect())
    print(wr())

bar()
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
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.collect())
