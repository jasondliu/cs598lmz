import weakref
# Test weakref.ref() with a class

class C(object):
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)

c = None
print(r())

print(r() is None)
# Test weakref.ref() with a class instance

class C(object):
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)

c = None
print(r())

print(r() is None)
# Test weakref.ref() with an old-style class

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)

c = None
print(r())

print(r() is None)
# Test weakref.ref() with an old-style class instance

class C:
    pass

c = C()
