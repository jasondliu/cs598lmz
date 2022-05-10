import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print('o:', o)
print('r:', r)
print('r():', r())

o2 = C()
r2 = weakref.ref(o2)

print('o2:', o2)
print('r2:', r2)
print('r2():', r2())

o = o2 = None

print('r():', r())
print('r2():', r2())

# Test weakref.WeakKeyDictionary()

class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1

print(d[o])

o = None

try:
    print(d[o])
except KeyError as e:
    print('KeyError', e)

# Test weakref.WeakValueDictionary()

class C:
    pass

o = C()
d = weakref.WeakValueDictionary()
