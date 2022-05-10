import weakref
# Test weakref.ref() for a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)

print(r().__class__)

# Test weakref.ref() for a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)

print(r().__class__)
