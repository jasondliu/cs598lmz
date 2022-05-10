import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o is o2)

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)

o2 = p
print(o is o2)

del o
#print(p)

del o2
#print(p)

# Test weakref.getweakrefcount() and weakref.getweakrefs()

o = C()

r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)

print(weakref.getweakrefcount(o))
print(weakref.getweakrefs(o))

del r1
del r2
del r3

print(weakref.getweakrefcount(o))
