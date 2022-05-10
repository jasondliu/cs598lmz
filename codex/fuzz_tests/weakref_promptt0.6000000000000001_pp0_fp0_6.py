import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print r() is f

f = None
print r() is None

# Test weakref.proxy()

class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
print p is f

f = None
try:
    p.bar
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()

class Foo:
    pass

f = Foo()
print weakref.getweakrefcount(f), weakref.getweakrefcount(Foo)

# Test weakref.getweakrefs()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print r in weakref.getweakrefs(f)

# Test weakref.finalize()

class Foo:
    pass

f = Foo()
def callback(r):
    print "callback"

weakref.finalize(f, callback)

f
