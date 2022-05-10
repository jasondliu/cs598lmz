import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(r2() is o2)

o = None
print(r())
print(r2())

print(r() is r2())

# Test weakref.getweakrefcount()

class D:
    pass

o = D()
d = weakref.WeakValueDictionary()
d[1] = o
d[2] = o
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

class E:
    pass

o = E()
d = weakref.WeakValueDictionary()
d[1] = o
d[2] = o
r = weakref.ref(o)
l = [o]
print(len(weakref.getweakrefs(o
