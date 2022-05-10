import weakref
# Test weakref.ref(x)
class Foo:
    pass
f = Foo()
r = weakref.ref(f)
print(r)
# Test weakref.proxy(x)
p = weakref.proxy(f)
print(p)
print(p.__class__)
# Test weakref.getweakrefcount(x)
print(weakref.getweakrefcount(f))
# Test weakref.getweakrefs(x)
print(weakref.getweakrefs(f))
# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
d[f] = 1
print(d)
del f
print(d)
# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
d[1] = f
print(d)
del f
print(d)
# Test weakref.finalize
f = Foo()
r = weakref.finalize(f, lambda: print('finalized'))
print(r)
del f
print(r)
print(r.alive)
# Test weak
