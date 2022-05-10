import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print(r, r())
del o
print(r, r())

# Test weakref.WeakKeyDictionary()
class C:
    pass
d = weakref.WeakKeyDictionary()
o1 = C()
o2 = C()
d[o1] = 1
d[o2] = 2
print(d)
del o1
print(d)

# Test weakref.WeakValueDictionary()
class C:
    pass
d = weakref.WeakValueDictionary()
o1 = C()
o2 = C()
d[1] = o1
d[2] = o2
print(d)
del o1
print(d)

# Test weakref.finalize()
class C:
    pass
o = C()
r = weakref.finalize(o, lambda o: print(o))
print(r)
del o
print(r)

# Test weakref.WeakSet()
class C:
    pass

