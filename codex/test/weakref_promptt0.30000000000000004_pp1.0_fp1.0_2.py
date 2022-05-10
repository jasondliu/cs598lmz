import weakref
# Test weakref.ref(obj)

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

del f
print(r())

# Test weakref.getweakrefcount(obj)

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefcount(f))

# Test weakref.getweakrefs(obj)

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(weakref.getweakrefs(f))

# Test weakref.proxy(obj)

class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
print(p)

del f
print(p)

# Test weakref.WeakKeyDictionary

class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1
print(d[f])

del f
