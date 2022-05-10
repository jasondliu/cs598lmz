import weakref
# Test weakref.ref()
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

o = C(42)
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

print(r() is None)
del o
print(r() is None)
# Test weakref.proxy()
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

o = C(42)
p = weakref.proxy(o)
print(p)
print(p.x)
print(p.x is o.x)

print(p is o)
del o
print(p.x)
# Test weakref.finalize()
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
