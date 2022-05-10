import weakref
# Test weakref.ref() with a class instance.
import weakref
import gc

class C:
    pass

c = C()
r = weakref.ref(c)
print r
print r()

c2 = C()
r2 = weakref.ref(c2)
print r2
print r2()

c = None
gc.collect()
print r
print r()
print r2
print r2()

# Test weakref.ref() with a class instance and __slots__.
import weakref
import gc

class C:
    __slots__ = ["a"]

c = C()
r = weakref.ref(c)
print r
print r()

c2 = C()
r2 = weakref.ref(c2)
print r2
print r2()

c = None
gc.collect()
print r
print r()
print r2
print r2()

# Test weakref.ref() with a class instance and __slots__ and __weakref__.
import weakref
import gc

class C:
