import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    def __init__(self):
        self.b = B(self)
        self.wr = weakref.ref(self)

class B:
    def __init__(self, a):
        self.a = a

a = A()
del a
gc.collect()

# Test gc.collect() with weakrefs and a callback

class A:
    def __init__(self):
        self.b = B(self)
        self.wr = weakref.ref(self, self.callback)
    def callback(self, wr):
        self.wr_cb = wr

class B:
    def __init__(self, a):
        self.a = a

a = A()
del a
gc.collect()

# Test gc.collect() with weakrefs and a callback that raises

class A:
    def __init__(self):
        self.b = B(self)
        self.wr = weakref.ref(self, self.callback)
    def callback(
