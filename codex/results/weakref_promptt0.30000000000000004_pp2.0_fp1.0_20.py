import weakref
# Test weakref.ref()
import weakref
class Foo(object):
    pass
f = Foo()
r = weakref.ref(f)
print r
print r()
print r() is f
print r() is None
del f
print r() is None

# Test weakref.proxy()
import weakref
class Foo(object):
    pass
f = Foo()
p = weakref.proxy(f)
print p
print p is f
print p is None
del f
print p is None

# Test weakref.getweakrefcount()
import weakref
class Foo(object):
    pass
f = Foo()
r = weakref.ref(f)
print weakref.getweakrefcount(f)
print weakref.getweakrefcount(r)

# Test weakref.getweakrefs()
import weakref
class Foo(object):
    pass
f = Foo()
r = weakref.ref(f)
print weakref.getweakrefs(f)
print weakref.getweakrefs(r)

# Test weakref.WeakKeyDictionary()
