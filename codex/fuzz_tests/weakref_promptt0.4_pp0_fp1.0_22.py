import weakref
# Test weakref.ref()
class C:
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
o = None
print r()
print r2()

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)
print p
print p is o
o2 = C()
p2 = weakref.proxy(o2)
print p2
print p2 is o2
o = None
try:
    print p
except ReferenceError:
    print "ReferenceError"
try:
    print p2
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
o = C()
print weakref.getweakrefcount(o)
r = weakref.ref(o)
print weakref.getweakrefcount(o)
r2 = weakref.ref(o)
print weakref.
