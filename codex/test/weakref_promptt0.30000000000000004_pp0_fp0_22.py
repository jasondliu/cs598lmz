import weakref
# Test weakref.ref()

class Foo(object):
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
print(r())

# Test weakref.proxy()

class Foo(object):
    pass

f = Foo()
p = weakref.proxy(f)
print(p)
print(p.__class__)

del f
print(p)

# Test weakref.getweakrefcount()

class Foo(object):
    pass

f = Foo()
print(weakref.getweakrefcount(f))

r = weakref.ref(f)
print(weakref.getweakrefcount(f))

p = weakref.proxy(f)
print(weakref.getweakrefcount(f))

# Test weakref.getweakrefs()

class Foo(object):
    pass

f = Foo()
print(weakref.getweakrefs(f))

r = weakref.ref(f)
