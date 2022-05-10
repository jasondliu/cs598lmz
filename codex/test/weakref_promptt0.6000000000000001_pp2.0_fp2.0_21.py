import weakref
# Test weakref.ref()
class C(object):
    pass
o = C()
r = weakref.ref(o)
print(r)
o2 = r()
print(o2 is o)
o2 = None
print(r)
o3 = r()
print(o3 is o)
o3 = None
print(r)
print(r() is None)
# Test weakref.WeakKeyDictionary()
class C(object):
    pass
o = C()
r = weakref.WeakKeyDictionary()
print(r)
r[o] = 1
print(r)
o2 = r.keys()[0]
print(o2 is o)
o2 = None
print(r)
o3 = r.keys()[0]
print(o3 is o)
o3 = None
print(r)
print(len(r.keys()) == 0)
# Test weakref.WeakValueDictionary()
class C(object):
    pass
o = C()
r = weakref.WeakValueDictionary()
print(r)
r[1]
