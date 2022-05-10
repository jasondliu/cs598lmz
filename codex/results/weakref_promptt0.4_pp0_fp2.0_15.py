import weakref
# Test weakref.ref()

class A(object):
    pass

a = A()

# Test weakref.ref()
r = weakref.ref(a)
print(r)
print(r())

# Test weakref.proxy()
p = weakref.proxy(a)
print(p)
print(p.__class__)

# Test weakref.getweakrefcount()
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
print(weakref.getweakrefs(a))

# Test weakref.finalize()
def callback(r):
    print("callback called")

r = weakref.finalize(a, callback)
print(r)

# Test weakref.WeakKeyDictionary()
d = weakref.WeakKeyDictionary()
d[a] = 1
print(d)
print(d[a])

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
d[1] = a
print(d)
print(d[1])
