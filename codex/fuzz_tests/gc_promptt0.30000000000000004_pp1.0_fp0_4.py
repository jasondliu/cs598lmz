import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to a class instance.
class A:
    pass
a = A()
r = weakref.ref(a)
del a
gc.collect()
print r() is None
# Test gc.collect() with a weakref to a class instance with a __del__ method.
class B:
    def __del__(self):
        pass
b = B()
r = weakref.ref(b)
del b
gc.collect()
print r() is None
# Test gc.collect() with a weakref to a class instance with a __del__ method
# that raises an exception.
class C:
    def __del__(self):
        raise Exception
c = C()
r = weakref.ref(c)
del c
try:
    gc.collect()
except:
    pass
print r() is None
# Test gc.collect() with a weakref to a class instance with a __del__ method
# that raises an exception that is caught by an outer exception handler.
class D:
    def __del__(self):
        raise Exception

