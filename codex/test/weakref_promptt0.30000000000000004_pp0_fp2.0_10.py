import weakref
# Test weakref.ref(obj)

import weakref

class Foo:
    pass

a = Foo()
r = weakref.ref(a)

print(r)
print(r())

del a
print(r())

a = Foo()
print(r())

print(r() is a)

print(r() is None)

print(r() is not None)

print(r() is not a)

print(r() is not b)

print(r() is not c)

print(r() is not d)

print(r() is not e)

print(r() is not f)

print(r() is not g)

print(r() is not h)

print(r() is not i)

print(r() is not j)

print(r() is not k)

print(r() is not l)

print(r() is not m)

print(r() is not n)

print(r() is not o)

print(r() is not p)

