import weakref
# Test weakref.ref(object)

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())
print(r() is o)
print(r() is None)

del o
print(r() is None)

# Test weakref.ref(object, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda r: print('callback called with', r))

print(r)
print(r())
print(r() is o)
print(r() is None)

del o
print(r() is None)

# Test weakref.proxy(object[, callback])

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)
print(p is o)
print(p is None)

del o
print(p is None)

# Test weakref.getweakrefcount(object)

class C:
    pass

o = C()
r = weakref
