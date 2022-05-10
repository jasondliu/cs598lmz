import weakref
# Test weakref.ref()

class A:
    pass

a = A()
w = weakref.ref(a)
print(w)
print(w())
print(w() is a)

# Test weakref.proxy()

a = A()
p = weakref.proxy(a)
print(p)
print(p is a)

# Test weakref.getweakrefcount()

a = A()
w1 = weakref.ref(a)
w2 = weakref.ref(a)
w3 = weakref.ref(a)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()

a = A()
w1 = weakref.ref(a)
w2 = weakref.ref(a)
w3 = weakref.ref(a)
print(weakref.getweakrefs(a))

# Test weakref.finalize()

a = A()
def callback(arg):
    print('callback({})'.format(arg))

