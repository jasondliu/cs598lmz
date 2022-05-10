import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())

o2 = r()
print(o2)
print(o2 is o)

o3 = C()
r2 = weakref.ref(o3)
print(r2())
print(o3 is o)

o3 = None
print(r2())

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o = C()
d['x'] = o
print(d['x'])

o2 = d['x']
print(o2 is o)

o3 = C()
d['x'] = o3
print(d['x'])
print(o3 is o)

o3 = None
print(d['x'])

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o = C()
d[o] = 42
print(d[o])

o2 = d.keys()[0]
