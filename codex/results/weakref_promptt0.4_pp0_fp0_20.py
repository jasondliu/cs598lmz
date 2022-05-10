import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
print type(r)
print r() is o
del o
gc.collect()
print r()

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)
print type(p)
print p is o
del o
try:
    p.foo
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
print weakref.getweakrefcount(o)
del r1
print weakref.getweakrefcount(o)
del r2
print weakref.getweakrefcount(o)

# Test weakref.getweakrefs()
o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
print weakref.getweakrefs(o)
del r1
print weakref.get
