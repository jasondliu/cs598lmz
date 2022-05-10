import weakref
# Test weakref.ref()

class A:
    pass

a = A()
r = weakref.ref(a)

print(r)
print(r())

del a

print(r)
print(r())

# Test weakref.WeakKeyDictionary

class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1

print(d)
print(d[a])

del a

print(d)

# Test weakref.WeakValueDictionary

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d[1] = a

print(d)
print(d[1])

del a

print(d)

# Test weakref.WeakSet

class A:
    pass

a = A()
s = weakref.WeakSet()
s.add(a)

print(s)
print(a in s)

del a

print(s)
print(a in s)

#
