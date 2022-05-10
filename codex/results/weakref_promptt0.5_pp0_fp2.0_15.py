import weakref
# Test weakref.ref
import gc

class A:
    pass

class B:
    pass

a = A()
b = B()
a.attr = b
b.attr = a

r = weakref.ref(a)
print r() is a
print r().attr is b
print r().attr.attr is a

del a
del b
gc.collect()
print r() is None

# Test weakref.proxy
import weakref

class A:
    pass

a = A()
p = weakref.proxy(a)
print p is a
print p.__class__ is A

del a
try:
    print p
except ReferenceError:
    pass
else:
    print "Expected ReferenceError"

# Test weakref.getweakrefcount
import weakref

class A:
    pass

a = A()
print weakref.getweakrefcount(a) == 0
w = weakref.ref(a)
print weakref.getweakrefcount(a) == 1
w2 = weakref.ref(a)
print
