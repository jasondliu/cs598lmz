import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

print(r() is o)
print(r() is None)

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda r: print('dead'))
print(r)
print(r())
print(o)

print(r() is o)
print(r() is None)

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
r = weakref.ref(o, lambda r: print('dead'))
print(r)
print(r())
print(o)

print(r() is o)
print(r() is None)

# Test weakref.ref(obj, callback)

class C:
    pass

o = C()
