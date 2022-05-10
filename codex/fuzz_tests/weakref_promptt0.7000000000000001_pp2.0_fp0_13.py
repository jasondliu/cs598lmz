import weakref
# Test weakref.ref

class A:
    pass

a = A()
r = weakref.ref(a)

print(a is r())
del a
print(r())
del r
# Test weakref.WeakKeyDictionary

class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1

print(d[a])
del a
print(d)
# Test weakref.WeakValueDictionary

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d['a'] = a

print(d['a'] is a)
del a
print(d)
# Test weakref.WeakValueDictionary

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d['a'] = a

print(d['a'] is a)
del a
print(d)
# Test weakref.WeakValueDictionary with list

class A:
    pass

a = A()
d = weakref.
