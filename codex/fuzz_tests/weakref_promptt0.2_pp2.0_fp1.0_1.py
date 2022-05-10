import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

o = o2 = None
print(r())
print(r2())

# Test weakref.ref() with a class instance and a callback.

class C:
    pass

def callback(r):
    print('callback(', r, ')')

o = C()
r = weakref.ref(o, callback)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, callback)
print(r2)
print(r2())

o = o2 = None
print(r())
print(r2())

# Test weakref.ref() with an old-style class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
