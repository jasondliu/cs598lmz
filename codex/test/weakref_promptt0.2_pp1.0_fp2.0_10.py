import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

del o
#print(p)

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
d = {1:1, 2:2, 3:3}
l = [o, d] * 100

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(d))
print(weakref.getweakrefcount(l))

# Test weakref.getweakrefs()

class C:
    pass

o = C()
d = {1:1, 2:2, 3:3}
l = [o, d] * 100

print(weakref.getweakrefs(o))
