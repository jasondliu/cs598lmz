import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o is o2)

del o
print(r())

del o2
print(r())

# Test weakref.WeakValueDictionary

class C:
    pass

o = C()
d = weakref.WeakValueDictionary()
d['x'] = o
print(d['x'])

del o
print(d['x'])

# Test weakref.WeakKeyDictionary

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1
print(d[o])

del o
try:
    print(d[o])
except KeyError:
    print("KeyError")

# Test weakref.WeakSet

class C:
    pass

o = C()
s = weakref.WeakSet()
s.add(o)
