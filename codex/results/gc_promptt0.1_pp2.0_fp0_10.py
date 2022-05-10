import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print "bar"

f = Foo()
f.x = bar
f.y = weakref.ref(f)

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
print gc.collect()
print gc.collect()
print gc.collect()
print gc.collect()
