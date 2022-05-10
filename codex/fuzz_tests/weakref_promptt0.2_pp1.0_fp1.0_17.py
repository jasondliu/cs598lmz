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

# Test weakref.WeakValueDictionary()

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
print(d['primary'])

# Test weakref.WeakKeyDictionary()

class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 'primary'
print(d[a])

del a
print(d[a])

# Test weakref.WeakSet()

class A:
    pass

a = A()
s = weakref.WeakSet()
s.add(a)
print(a in s)

del a
print(a in s)

# Test weakref.finalize()

class A:
    pass


