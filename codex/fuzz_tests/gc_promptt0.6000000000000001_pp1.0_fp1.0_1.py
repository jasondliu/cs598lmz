import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a class instance
class C(object):
    pass

c = C()
r = weakref.ref(c)
gc.collect()

# Test gc.collect() with a weakref to a callable
def f():
    pass

r = weakref.ref(f)
gc.collect()

# Test gc.collect() with a weakref to a callable and bound method
class C(object):
    def f(self):
        pass


c = C()
r = weakref.ref(c.f)
gc.collect()

# Test gc.collect() with a weakref to an instance method
class C(object):
    def f(self):
        pass


c = C()
r = weakref.ref(c.f)
gc.collect()

# Test gc.collect() with a weakref to a class object
class C(object):
    pass


r = weakref.ref(C)
gc.collect()

# Test gc.collect() with a weakref to a generator
def f
