import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r
print r()
print type(r)
print type(r())
print r is o
print r() is o

r2 = weakref.ref(o)
print r2
print r2()
print type(r2)
print type(r2())
print r2 is o
print r2() is o

o2 = C()
r3 = weakref.ref(o2)
print r3
print r3()
print type(r3)
print type(r3())
print r3 is o2
print r3() is o2

print r is r2
print r is r3
print r2 is r3

print r == r2
print r == r3
print r2 == r3

print r is None
print r2 is None
print r3 is None

print r() is None
print r2() is None
print r3() is None

del o
print r
print r()
print type
