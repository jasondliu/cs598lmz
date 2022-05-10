import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('dying', x))
print(r2)
print(r2())

del o2
print(r2)
print(r2())

# Test weakref.proxy

class D:
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return '<D %d>' % self.n

o = D(42)
p = weakref.proxy(o)
print(p)

# test weakref.finalize

class E:
    def __init__(self):
        self.n = 42
        self.finalizer = weakref.finalize(self, self.finalize)
    def finalize(self):
        print('dying', self.n)

e = E()
