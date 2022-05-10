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

print("\n")

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.x)

del o
print(p.x)

print("\n")

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
d = {1:1, 2:2, 3:3}
l = [o, d]

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(d))
print(weakref.getweakrefcount(l))

print("\n")

# Test weakref.getweakrefs()

class C:
    pass

o = C()
d = {1:1, 2:2, 3:3}
l
