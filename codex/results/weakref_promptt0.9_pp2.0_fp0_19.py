import weakref
# Test weakref.ref
class C(object):
    pass

wr = weakref.ref(C)
print wr

print weakref.getweakrefcount(C)
wr = weakref.ref(C)
print weakref.getweakrefcount(C)

print wr() is C

wr = weakref.ref(C)
print weakref.getweakrefcount(C)
del wr
print weakref.getweakrefcount(C)


# Test weakref.WeakValueDictionary
a = []
d = weakref.WeakValueDictionary()

d[1] = C()
d[2] = C()

print len(d)
d[1].__del__()
print len(d)

d[2] = None
print len(d)
