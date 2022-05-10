import weakref
# Test weakref.ref() on a function.
import gc

def f():
    pass

r = weakref.ref(f)
print r() is f
print r()
gc.collect()
print r() is f
print r()

# Test weakref.proxy() on a function.
p = weakref.proxy(f)
print p is f
print p
gc.collect()
print p is f
print p

# Test weakref.ref() on a class.
class C:
    pass

r = weakref.ref(C)
print r() is C
print r()
gc.collect()
print r() is C
print r()

# Test weakref.proxy() on a class.
p = weakref.proxy(C)
print p is C
print p
gc.collect()
print p is C
print p

# Test weakref.ref() on a class instance.
c = C()
r = weakref.ref(c)
print r() is c
print r()
gc.collect()
print r() is c
print r()

# Test
