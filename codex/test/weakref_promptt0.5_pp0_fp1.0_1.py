import weakref
# Test weakref.ref(instance)
# Test weakref.ref(instance, callback)
# Test weakref.proxy(instance)
# Test weakref.getweakrefs(instance)
# Test weakref.getweakrefcount(instance)
# Test weakref.ref(instance, callback)

class C:
    pass

def callback(x):
    print('callback called with', x)

def callback2(x):
    print('callback2 called with', x)

def callback3(x):
    print('callback3 called with', x)

c = C()

p = weakref.proxy(c)
print(p)

r = weakref.ref(c, callback)
print(r)

r2 = weakref.ref(c, callback2)
print(r2)

r3 = weakref.ref(c, callback3)
print(r3)

print(weakref.getweakrefcount(c))
print(weakref.getweakrefs(c))

del c

print(weakref.getweakrefcount(p))
print
