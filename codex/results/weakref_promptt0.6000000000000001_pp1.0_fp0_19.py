import weakref
# Test weakref.ref with a weak dictionary
import _weakref

class C:
    pass

def callback(reference):
    print 'called back with', reference

d = weakref.WeakKeyDictionary()
o = C()
r = weakref.ref(o, callback)
d[o] = 1
print d[o]
del o
print d.data
print d.data.values()
