import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)

print r
print r()
print r() is o

o2 = C()
r2 = weakref.ref(o2)

print r2
print r2()
print r2() is o2

print r()
print r() is o

del o2
print r2()

del o
print r()

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print p
print p is o

o2 = C()
p2 = weakref.proxy(o2)

print p2
print p2 is o2

print p
print p is o

del o2
print p2

del o
print p
