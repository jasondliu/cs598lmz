import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after creating a cyclic object with __del__() methods.

class C1:
    def __init__(self, name):
        self.name = name
        self.w = weakref.ref(self)

    def __del__(self):
        del self.w

class C2:
    def __init__(self, name):
        self.name = name
        self.w = weakref.ref(self)

    def __del__(self):
        global c
        del c

# act as if this is the module
class _:
    __name__ = '__main__'
    c = C1('c')
c = C2('c')
del _
gc.collect()
gc.collect()
