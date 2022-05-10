import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)

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

print(wkd[b1])
print(wkd[b2])

del b1

print(wkd[b2])

try:
    print(wkd[b1])
except KeyError:
    print("b1 is gone")

del b2

try:
    print(wkd[b2])
except KeyError:
    print("b2 is gone")

# Test weakref.WeakValueDictionary()

class C:
    pass

c1 = C()
c2 = C()
c3 = C()

wvd = weakref.WeakValue
