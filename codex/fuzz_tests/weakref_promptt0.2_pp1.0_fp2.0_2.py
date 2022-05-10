import weakref
# Test weakref.ref(x)

class C:
    pass

c = C()
r = weakref.ref(c)

print(r())

del c

print(r())

# Test weakref.ref(x, callback)

class C:
    pass

c = C()

def callback(r):
    print('callback called')

r = weakref.ref(c, callback)

print(r())

del c

print(r())

# Test weakref.proxy(x)

class C:
    pass

c = C()
p = weakref.proxy(c)

print(p)

del c

print(p)

# Test weakref.getweakrefcount(x)

class C:
    pass

c = C()

print(weakref.getweakrefcount(c))

r = weakref.ref(c)

print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs(x)

class C:
    pass


