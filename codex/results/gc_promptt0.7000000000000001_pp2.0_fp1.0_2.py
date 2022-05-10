import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().
# This is supposed to return the number of objects collected and
# deallocated, but it returns zero instead.  Bug #476106.

class C(object):
    def __init__(self, name):
        self.name = name

def f():
    a = C('a')
    l = [a]
    del l
    print gc.collect()

f()
f()
f()
print gc.collect()
