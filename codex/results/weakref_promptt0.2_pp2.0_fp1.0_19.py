import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

del o
print(r)
print(r())
