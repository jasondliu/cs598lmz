import weakref
# Test weakref.ref()

class C:
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        return 'C(%r)' % self.i

r = weakref.ref(C(1))
print(r)
print(r())

r = weakref.ref(C(2))
print(r)
print(r())

r = weakref.ref(C(3))
print(r)
print(r())

r = weakref.ref(C(4))
print(r)
print(r())

r = weakref.ref(C(5))
print(r)
print(r())

r = weakref.ref(C(6))
print(r)
print(r())

r = weakref.ref(C(7))
print(r)
print(r())

r = weakref.ref(C(8))
print(r)
print(r())

r = weakref.ref(C(9))
print(r)
print(r())

