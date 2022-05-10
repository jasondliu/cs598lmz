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

# Test weakref.WeakKeyDictionary()

class B:
    pass

b1 = B()
b2 = B()
b3 = B()

wkd = weakref.WeakKeyDictionary()
wkd[b1] = 1
wkd[b2] = 2
wkd[b3] = 3

print(wkd.data)

del b2

print(wkd.data)

del b1

print(wkd.data)

del b3

print(wkd.data)

# Test weakref.WeakValueDictionary()

class C:
    pass

c1 = C()
c2 = C()
c3 = C()

wvd = weakref.WeakValueDictionary()
wvd['c1'] = c1
wvd['c2'] = c2
wvd['c3'] = c
