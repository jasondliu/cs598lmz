import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref to an instance

class C:
    pass

w = weakref.ref(C())
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())

# Test gc.collect() with a weakref to a class

w = weakref.ref(C)
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())

# Test gc.collect() with a weakref to an instance method

class D:
    def f(self):
        pass

w = weakref.ref(D().f)
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())
#print(gc.collect())

# Test gc.collect() with a weakref to a class method

class E:
    @classmethod
    def f(cls):
        pass

w = weakref.ref(E.f)
#print(gc.collect())

