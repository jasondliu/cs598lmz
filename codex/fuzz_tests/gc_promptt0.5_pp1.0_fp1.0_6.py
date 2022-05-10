import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Test that gc.collect() returns the number of unreachable
# objects found.

class C:
    pass

class D:
    def __init__(self, x=C()):
        self.x = x

def f():
    c = C()
    d = D()
    c.x = d
    d.x = c
    del c, d

f()
c = C()
d = D()
c.x = d
d.x = c
gc.collect()
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
print gc
