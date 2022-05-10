import weakref
# Test weakref.ref() and weakref.proxy()

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r
print r()
print r() is o
print

p = weakref.proxy(o)
print p
print p is o
print

del o
print r()
print p

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
o1 = C()
o2 = C()
o3 = C()
d[o1] = 1
d[o2] = 2
d[o3] = 3
print d[o1], d[o2], d[o3]
del o2
print d[o1], d[o3]
del o1
print d[o3]
del o3
print d

# Test weakref.WeakValueDictionary

d = weakref.WeakValueDictionary()
o1 = C()
o2 = C()
o3 = C()
d[1] = o1
d[2] = o2
d
