import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations()
gc.collect_generations()
gc.collect()

# Test __del__
# Printed output will show the finalizer being called twice,
# once immediately and once again at the next collection
# with Python doing its finalizer ordering

class X:
    def __del__(self):
        print("X.__del__")

x = X()
w = weakref.ref(x)
x.a = w
del x
gc.collect()

# Test gc.disable()
# Test gc.isenabled()

gc.disable()
gc.collect()
print(gc.isenabled())
del x, w
print("initially disabled:", gc.garbage)

g = X()
g.x = X()
g.x.w = weakref.ref(g)
g.x.a = X()
g.x.a.b = X()
g.x.a.w = weakref.ref(g)
g.z = weakref.ref(g.x)

gc.enable()
print(gc.
