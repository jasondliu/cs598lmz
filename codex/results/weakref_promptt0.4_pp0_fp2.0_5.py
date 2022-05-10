import weakref
# Test weakref.ref()

class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'A(%r)' % self.x

a = A(42)
r = weakref.ref(a)
print(r())
print(r() is a)
print(r() is None)
a = None
print(r() is None)

# Test weakref.proxy()

a = A(42)
p = weakref.proxy(a)
print(p)
print(p is a)
print(p.x)
a = None
try:
    print(p.x)
except ReferenceError:
    print('ReferenceError')

# Test weakref.getweakrefcount()

a = A(42)
print(weakref.getweakrefcount(a))
r = weakref.ref(a)
print(weakref.getweakrefcount(a))
p = weakref.proxy(a)
print(weakref.getweakrefcount(a))
a = None

