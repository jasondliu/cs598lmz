import weakref
# Test weakref.ref()

import weakref

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())

c = 1
print(r())

c = C()
print(r())

print(r is weakref.ref(c))

print(r == weakref.ref(c))
print(r() == c)

print(r != weakref.ref(c))
print(r() != c)

print(r is not weakref.ref(c))
print(r() is not c)

print(r < weakref.ref(c))
print(r() < c)

print(r <= weakref.ref(c))
print(r() <= c)

print(r > weakref.ref(c))
print(r() > c)

print(r >= weakref.ref(c))
print(r() >= c)

# Test weakref.WeakKeyDictionary()

import weakref

class C:
    pass

c = C()

