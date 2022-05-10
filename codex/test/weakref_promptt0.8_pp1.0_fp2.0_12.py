import weakref
# Test weakref.ref.
Base = object
class A(Base):
    pass

a = A()
r = weakref.ref(a)
print(r)

a2 = r()
print(a2)
print(a2 == a)
print(a2 is a)

# Test weakref.WeakKeyDictionary.
d = weakref.WeakKeyDictionary()
d[a] = 'something'
print(d[a])
d[a2] = 'something else'
print(d[a2])
print(d[a])

a = None
print(d.get(a))

a2 = None
print(d.get(a2))
print(d.get(a))

l = list(d)
print(l)
print(len(l) == 0)

# Test weakref.WeakValueDictionary.
d = weakref.WeakValueDictionary()
d[a] = 'something'
print(d[a])
d[a2] = 'something else'
print(d[a2])
