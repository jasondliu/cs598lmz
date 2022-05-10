import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

print(r is r2)
print(r() is r2())

print(r() is o)
print(r2() is o2)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

print(p is p2)
print(p is o)
print(p2 is o2)

# Test weakref.getweakrefcount() and weakref.getweakrefs()

o = C()
print(weakref.getweakrefcount(o))
print(weakref.getweakrefs(o))

r = weakref.ref(o)
