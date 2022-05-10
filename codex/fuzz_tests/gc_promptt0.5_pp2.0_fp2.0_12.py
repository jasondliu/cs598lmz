import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a weakref to an instance with a __del__ method

class A:
    def __del__(self):
        print "del"

a = A()
r = weakref.ref(a)
a = None

gc.collect()
print r()

del a
gc.collect()
print r()

del r
gc.collect()
print gc.collect()

# Test gc.collect with a weakref to an instance with a __del__ method
# that raises an exception

class A:
    def __del__(self):
        print "del"
        raise RuntimeError

a = A()
r = weakref.ref(a)
a = None

gc.collect()
print r()

del a
gc.collect()
print r()

del r
gc.collect()
print gc.collect()

# Test gc.collect with a weakref to an instance with a __del__ method
# that raises an exception that is caught

class A:
    def __del__(self):
        print "del"
       
