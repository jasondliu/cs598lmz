import weakref
# Test weakref.ref() with a class instance.

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.ref() with a class instance and a callback.

def callback(r):
    print('callback(', r, ')')

o = C()
r = weakref.ref(o, callback)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.ref() with a class instance, a callback, and a dictionary.

def callback(r):
    print('callback(', r, ')')

o = C()
d = {}
r = weakref.ref(o, callback, d)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.ref() with a class instance and a dictionary.

o = C()
d = {}
r
