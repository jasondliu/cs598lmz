import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

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

del o
print(p)
