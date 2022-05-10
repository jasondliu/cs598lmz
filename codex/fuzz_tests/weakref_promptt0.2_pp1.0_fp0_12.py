import weakref
# Test weakref.ref(obj)

class C(object):
    pass

obj = C()
r = weakref.ref(obj)
print(r)
print(r())

del obj
print(r())

# Test weakref.ref(obj, callback)

def callback(r):
    print('callback(', r, ')')

obj = C()
r = weakref.ref(obj, callback)
print(r)
print(r())

del obj
print(r())

# Test weakref.proxy(obj, callback)

def callback(p):
    print('callback(', p, ')')

obj = C()
p = weakref.proxy(obj, callback)
print(p)
print(p.__class__)

del obj
print(p)

# Test weakref.getweakrefcount(obj)

obj = C()
print(weakref.getweakrefcount(obj))

r = weakref.ref(obj)
print(weakref.getweakrefcount(obj))

r = weakref.ref
