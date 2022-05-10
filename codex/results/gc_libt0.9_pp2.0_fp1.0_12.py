import gc, weakref

gc.set_debug(gc.DEBUG_COLLECTABLE)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
gc.set_debug(gc.DEBUG_INSTANCES)
gc.set_debug(gc.DEBUG_OBJECTS)
gc.set_debug(gc.DEBUG_SAVEALL)
gc.set_debug(gc.DEBUG_LEAK)

class A:
    pass

a = A()
b = A()
c = A()
print(gc.collect())
t = weakref.WeakValueDictionary()
d = A()
t["yo"] = d
print(gc.collect())
print(t)
e = A()
