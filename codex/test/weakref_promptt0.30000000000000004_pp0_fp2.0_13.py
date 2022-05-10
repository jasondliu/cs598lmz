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

class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1
print(d[a])
del a
try:
    print(d[a])
except KeyError:
    print("KeyError")

# Test weakref.WeakValueDictionary()

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d['a'] = a
print(d['a'])
del a
try:
    print(d['a'])
except KeyError:
    print("KeyError")

# Test weakref.WeakSet()

class A:
    pass

a = A()
s = weakref.WeakSet()
s.add(a)
print(a in s)
del a
print(a in s)
