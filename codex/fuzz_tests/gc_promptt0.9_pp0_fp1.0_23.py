import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a few objects with a __del__ in the mix.
# Shouldn't crash.

class C:
    def __del__(self):
        if b:
            raise Exception, 43

def f1():
    a = C()
    gc.collect()
    b.append(42)

def f2():
    a = C()
    gc.collect()
    b.append(43)

b = []
f1()
f2()
