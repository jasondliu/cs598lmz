import weakref
# Test weakref.ref()

class C:
    pass

obj = C()
r = weakref.ref(obj)

print(r)
print(r())

obj2 = C()
r2 = weakref.ref(obj2)
print(r2)
print(r2())

obj = obj2 = None
print(r())
print(r2())

# Test weakref.WeakValueDictionary

class C:
    pass

a = C()
b = C()
c = C()

d = weakref.WeakValueDictionary()
d['a'] = a
d['b'] = b
d['c'] = c

print(d['a'])
print(d['b'])
print(d['c'])

a = b = c = None

print(d['a'])
print(d['b'])
print(d['c'])

# Test weakref.WeakKeyDictionary

class C:
    pass

a = C()
b = C()
c = C()

d = weakref.
