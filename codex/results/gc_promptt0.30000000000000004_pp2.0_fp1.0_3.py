import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an object with a __del__ method.
class A:
    def __del__(self):
        pass

a = A()
w = weakref.ref(a)
gc.collect()
print(w())

# Test gc.collect() with a weakref to an object with a __del__ method
# that raises an exception.
class B:
    def __del__(self):
        raise Exception

b = B()
w = weakref.ref(b)
gc.collect()
print(w())

# Test gc.collect() with a weakref to an object with a __del__ method
# that raises an exception that is caught by the weakref machinery.
class C:
    def __del__(self):
        try:
            raise Exception
        except:
            pass

c = C()
w = weakref.ref(c)
gc.collect()
print(w())

# Test gc.collect() with a weakref to an object with a __del__ method
# that raises an exception that is caught by the weakref
