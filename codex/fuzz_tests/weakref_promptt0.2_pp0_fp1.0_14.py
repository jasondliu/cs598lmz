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

# Test weakref.WeakValueDictionary

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
print(d['primary'])
