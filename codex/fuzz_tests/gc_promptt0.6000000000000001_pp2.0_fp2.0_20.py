import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a

def f():
    x = A()

gc.collect()
print gc.collect()
f()
print gc.collect()

# Test gc.get_debug().
print gc.get_debug()

# Test gc.set_debug().
gc.set_debug(gc.DEBUG_STATS)
print gc.get_debug()
gc.set_debug(gc.DEBUG_LEAK)
print gc.get_debug()
gc.set_debug(0)
print gc.get_debug()

# Test gc.get_objects().
print len(gc.get_objects())

# Test gc.get_referrers().
class C: pass
c = C()
print len(gc.get_referrers(c))

# Test gc.get_referents().
print len(gc.get_
