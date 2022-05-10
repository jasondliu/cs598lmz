import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
w = weakref.ref(a)

gc.collect()
print gc.garbage

del a
gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print w()

gc.collect()
print gc.garbage

print
