import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print r() is o
print r() is None

del o
gc.collect()

print r() is None

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)

print p is o
print p.__class__ is C

del o
try:
    p.foo
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount() and weakref.getweakrefs()
class D:
    pass

a = D()
b = D()
c = D()

wr1 = weakref.ref(a)
wr2 = weakref.ref(a)
wr3 = weakref.ref(a)
wr4 = weakref.ref(b)
wr5 = weakref.ref(c)

print weakref.getweakrefcount(a)
print weakref.getweakrefcount(b)
print weakref.getweakrefcount
