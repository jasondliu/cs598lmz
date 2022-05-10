import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

del o
print(r())

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print(r() is None)

print
