import weakref
# Test weakref.ref()

class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'A(%r)' % self.x

class B:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'B(%r)' % self.x

a = A(1)
b = B(a)

r = weakref.ref(a)
print(r)
print(r())
print(r() is a)

r = weakref.ref(b)
print(r)
print(r())
print(r() is b)

r = weakref.ref(b.x)
print(r)
print(r())
print(r() is b.x)

r = weakref.ref(b.x.x)
print(r)
print(r())
print(r() is b.x.x)

# Test weakref.ref(self)

class C:
    def
