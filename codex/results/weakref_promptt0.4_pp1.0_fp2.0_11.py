import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)

print(r())
print(r() is c)

del c
print(r())

# Test weakref.WeakKeyDictionary

class C:
    pass

c1 = C()
c2 = C()
c3 = C()

d = weakref.WeakKeyDictionary()
d[c1] = 1
d[c2] = 2
d[c3] = 3

print(d[c1])
print(d[c2])
print(d[c3])

del c2

print(d[c1])
print(d[c3])

# Test weakref.WeakValueDictionary

class C:
    pass

c1 = C()
c2 = C()
c3 = C()

d = weakref.WeakValueDictionary()
d[1] = c1
d[2] = c2
d[3] = c3

print(d[1])
print(d
