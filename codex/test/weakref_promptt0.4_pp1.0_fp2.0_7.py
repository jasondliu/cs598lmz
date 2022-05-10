import weakref
# Test weakref.ref

class A:
    pass

a = A()
w = weakref.ref(a)
print(w)
print(w())

del a
print(w())

print(w() is None)

# Test weakref.WeakKeyDictionary

class B:
    pass

b1 = B()
b2 = B()
b3 = B()

d = weakref.WeakKeyDictionary()
d[b1] = 1
d[b2] = 2
d[b3] = 3

print(d.items())

del b2

print(d.items())

print(d[b1])
print(d[b3])

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

print(d.items())

del c2

