import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)
print(r)
print(r())

del a
print(r())

# Test weakref.proxy()

class B:
    pass

b = B()
p = weakref.proxy(b)
print(p)
print(p.__class__)

del b
# print(p)

# Test weakref.WeakKeyDictionary()

class C:
    pass

c1 = C()
c2 = C()

d = weakref.WeakKeyDictionary()
d[c1] = 1
d[c2] = 2
print(d[c1])
print(d[c2])

del c1
print(d[c2])

# Test weakref.WeakValueDictionary()

class D:
    pass

d1 = D()
d2 = D()

e = weakref.WeakValueDictionary()
e[1] = d1
e[2] = d2
print(
