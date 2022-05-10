import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()
r = weakref.ref(a)

print(r)
print(r())

del a
print(r())

# Test weakref.WeakKeyDictionary()

class B(object):
    pass

b1 = B()
b2 = B()
b3 = B()

d = weakref.WeakKeyDictionary()
d[b1] = 1
d[b2] = 2
d[b3] = 3

print(d)

del b2
print(d)

# Test weakref.WeakValueDictionary()

class C(object):
    pass

c1 = C()
c2 = C()
c3 = C()

d = weakref.WeakValueDictionary()
d[1] = c1
d[2] = c2
d[3] = c3

print(d)

del c2
print(d)

# Test weakref.WeakSet()

class D(object):
    pass


