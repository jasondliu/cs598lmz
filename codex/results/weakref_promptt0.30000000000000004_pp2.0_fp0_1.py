import weakref
# Test weakref.ref() and weakref.proxy()

class C(object):
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print type(r)
print type(p)
print r() is o
print p is o

del o

print r() is None

try:
    p.foo
except ReferenceError:
    print "ReferenceError"
