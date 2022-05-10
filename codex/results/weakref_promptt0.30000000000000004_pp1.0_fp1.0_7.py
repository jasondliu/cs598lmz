import weakref
# Test weakref.ref()
class C(object):
    pass
o = C()
r = weakref.ref(o)
print r() is o
del o
print r() is None

# Test weakref.proxy()
class C(object):
    pass
o = C()
p = weakref.proxy(o)
print p is o
del o
try:
    p.foo
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
class C(object):
    pass
o = C()
print weakref.getweakrefcount(o)
r = weakref.ref(o)
print weakref.getweakrefcount(o)
p = weakref.proxy(o)
print weakref.getweakrefcount(o)

# Test weakref.getweakrefs()
class C(object):
    pass
o = C()
print weakref.getweakrefs(o)
r = weakref.ref(o)
print weakref.getweakrefs(o)
p = weakref.proxy(o)
print
