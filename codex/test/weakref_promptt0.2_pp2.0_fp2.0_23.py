import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('dead', x))
print(r2)
print(r2())

del o2
print(r2())

print(r())

del o
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2, lambda x: print('dead', x))
print(p2)

del o2
print(p2)

print(p)

del o
print(p)

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

