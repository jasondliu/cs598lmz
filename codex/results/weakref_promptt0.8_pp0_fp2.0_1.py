import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print 'o:', o
print 'r:', r
print 'r():', r()
print

o2 = C()
r2 = weakref.ref(o2, lambda u: print('callback for ', u))
print 'o2:', o2
print 'r2:', r2
print 'deleting o2'
del o2
gc.collect()  # no need to call this
print 'r2():', r2()
print

L = []
for i in range(4):
    o = C()
    r = weakref.ref(o, lambda u: L.append(u))
    print r, o
    print r(), o
print L


# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = C()
d['test'] = o
print d
print d['test']
print d
del o
gc.collect()  # no need to call this
print d
print d['test']

