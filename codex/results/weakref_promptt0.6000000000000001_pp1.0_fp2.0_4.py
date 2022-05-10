import weakref
# Test weakref.ref(Exception())

class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a

a = A()
wr = weakref.ref(a)
del a
print(wr())

a = A()
wr = weakref.ref(a.b)
del a
print(wr())

a = A()
wr = weakref.ref(a.b.a)
del a
print(wr())

a = A()
wr = weakref.ref(a.b.a.b)
del a
print(wr())
