import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    f = Foo()
    f.x = 1
    f.y = 2
    f.z = 3
    return f

f = bar()
f.x = 1
f.y = 2
f.z = 3

print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
print g
