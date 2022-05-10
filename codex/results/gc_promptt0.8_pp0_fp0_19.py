import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without global __del__

d = weakref.WeakKeyDictionary()

class A:
    def t(self):
        pass

a = A()
#d[a] = 1
gc.collect()
del a
gc.collect()
