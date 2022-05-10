import weakref
# Test weakref.ref(obj)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.ref(obj, callback)

def callback(r):
    print('callback({!r})'.format(r))

o = C()
r = weakref.ref(o, callback)
print(r)
print(r())
print(r() is o)
print(r() is None)

# Test weakref.proxy(obj)

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)
print(p is None)

# Test weakref.proxy(obj, callback)

def callback(p):
    print('callback({!r})'.format(p))

o = C()
p = weakref.proxy(o, callback)
print(p)
print(p is o)
print(p is None)

# Test weakref.
