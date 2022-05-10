import weakref
# Test weakref.ref
class C(object):
    pass

c = C()
r = weakref.ref(c)
print r
print r()
print r() is c
print c.__dict__
print r().__dict__
print r().__dict__ is c.__dict__

print c.__class__
print r().__class__
print r().__class__ is c.__class__

print c.__class__.__bases__
print r().__class__.__bases__
print r().__class__.__bases__ is c.__class__.__bases__

print c.__class__.__name__
print r().__class__.__name__
print r().__class__.__name__ is c.__class__.__name__

print c.__class__.__module__
print r().__class__.__module__
print r().__class__.__module__ is c.__class__.__module__

print c.__class__.__dict__
print r().__class__.__dict__
print r
