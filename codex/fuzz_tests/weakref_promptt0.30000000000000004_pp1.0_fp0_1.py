import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

print(r() is None)
del a
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

