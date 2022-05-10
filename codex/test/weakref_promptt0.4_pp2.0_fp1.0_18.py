import weakref
# Test weakref.ref(object)

def test(obj):
    ref = weakref.ref(obj)
    obj = None
    return ref()

class C: pass

c = C()
r = test(c)
print(r)

print(weakref.getweakrefcount(c))
print(weakref.getweakrefs(c))

print(weakref.ref(c))
print(weakref.proxy(c))

print(weakref.proxy(c) is c)
print(weakref.proxy(c) == c)

print(weakref.getweakrefcount(c))
print(weakref.getweakrefs(c))

print(weakref.getweakrefcount(weakref.proxy(c)))
print(weakref.getweakrefs(weakref.proxy(c)))

print(weakref.getweakrefcount(weakref.ref(c)))
print(weakref.getweakrefs(weakref.ref(c)))

print(weakref.getweakrefcount(r))
