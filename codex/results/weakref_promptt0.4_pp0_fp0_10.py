import weakref
# Test weakref.ref(obj)

class C:
    pass

obj = C()
r = weakref.ref(obj)
print(r)
print(r())

del obj
print(r)
print(r())

# Test weakref.ref(obj, callback)

def callback(r):
    print('callback called with', r)

obj = C()
r = weakref.ref(obj, callback)

del obj
print(r)

# Test weakref.proxy(obj, callback)

def callback(p):
    print('callback called with', p)

obj = C()
p = weakref.proxy(obj, callback)
print(p)

del obj
print(p)

# Test weakref.getweakrefcount(obj)

class C:
    pass

obj = C()
print(weakref.getweakrefcount(obj))

r = weakref.ref(obj)
print(weakref.getweakrefcount(obj))

# Test weakref.getweakrefs(obj)

class C:

