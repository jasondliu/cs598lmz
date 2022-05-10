import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print r
print r() is o
del o
print r() is None

# Test weakref.proxy()
class C:
    pass
o = C()
p = weakref.proxy(o)
print p
print p is o
del o
try:
    p.foo
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
class C:
    pass
o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
print weakref.getweakrefcount(o)
print weakref.getweakrefcount(o) == 2

# Test weakref.getweakrefs()
class C:
    pass
o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
print weakref.getweakrefs(o)
print weakref.getweakrefs(o) == [r1, r2]


