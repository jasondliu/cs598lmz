import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(r2() is o2)
print(r2() is None)

o = None
print(r())
print(r() is None)

o2 = None
print(r2())
print(r2() is None)

print(r2 == r)
print(r2 != r)

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o = C()
d['x'] = o
print(d['x'] is o)
o = None
print(d['x'] is None)

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
