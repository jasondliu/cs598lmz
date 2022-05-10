import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.proxy()

class D:
    pass

o = D()
p = weakref.proxy(o)
print(p)

o2 = D()
p2 = weakref.proxy(o2, lambda x: print('callback'))
print(p2)

del o2
print(p2)

# Test weakref.getweakrefcount()

class E:
    pass

o = E()
r = weakref.ref(o)
print(weakref.getweakrefcount(o))

o2 = E()
