import weakref
# Test weakref.ref(x)
class C(object):
    pass

c = C()
r = weakref.ref(c)
print type(r)
print r() is c
del c
print r() is None
# Test weakref.ref(x, callback)
class C(object):
    pass

c = C()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(c, callback)
print r() is c
del c
print r() is None
print l
print l[0] is r
# Test weakref.proxy(x)
class C(object):
    pass

c = C()
p = weakref.proxy(c)
print type(p)
print p is c
del c
try:
    print p
except ReferenceError:
    print "ReferenceError"
# Test weakref.getweakrefcount(x)
class C(object):
    pass

c = C()
print weakref.getweakrefcount(c)
r = weakref.ref(c)
print weakref.
