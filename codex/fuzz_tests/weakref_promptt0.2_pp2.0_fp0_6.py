import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r
print r() is o
print r() is None

del o
print r() is None

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print p
print p is o

del o
try:
    print p
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()

o = C()
print weakref.getweakrefcount(o)
r = weakref.ref(o)
print weakref.getweakrefcount(o)
del r
print weakref.getweakrefcount(o)

# Test weakref.getweakrefs()

o = C()
print weakref.getweakrefs(o)
r = weakref.ref(o)
print weakref.getweakrefs(o)
del r
print weakref.getweakrefs(o)

# Test weakref.WeakKeyDictionary


