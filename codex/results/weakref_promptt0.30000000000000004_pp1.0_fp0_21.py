import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

del o
print(r())

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda x: print("callback called"))
print(r)
print(r())
print(r() is o)

del o
print(r())

# Test weakref.WeakKeyDictionary(dict)

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary({o: 1})
print(d[o])

del o
print(d)

# Test weakref.WeakKeyDictionary()

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1
print(d[o])

del o
print(d)

# Test weakref.WeakValueD
