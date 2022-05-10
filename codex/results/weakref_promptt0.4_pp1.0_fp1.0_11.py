import weakref
# Test weakref.ref() with a class that has a __del__ method.
# The class instance is not garbage collected.

class C:
    def __del__(self):
        print "deleting C"

def f(x):
    print "x =", x

x = C()
r = weakref.ref(x, f)
print r
print r()
del x
import gc
gc.collect()
print r()
# Test weakref.ref() with a class that has a __del__ method.
# The class instance is not garbage collected.

class C:
    def __del__(self):
        print "deleting C"

def f(x):
    print "x =", x

x = C()
r = weakref.ref(x, f)
print r
print r()
del x
import gc
gc.collect()
print r()
# Test weakref.ref() with a class that has a __del__ method.
# The class instance is not garbage collected.

class C:
    def __del__(self):
        print
