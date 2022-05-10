import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('deleted'))
print(r2)
print(r2())

del o2
print(r2())

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda x: print('deleted'))
print(r)
print(r())

del o
print(r())

# Test weakref.proxy(obj)

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)

o2 = C()
p2 = weakref.proxy(o2, lambda x: print('deleted'))
print(p2)
print(p2.__class__)

del o2
