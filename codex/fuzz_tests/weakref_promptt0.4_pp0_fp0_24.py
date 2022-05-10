import weakref
# Test weakref.ref() with a cyclic reference
class A:
    pass
a = A()
a.b = a
wr = weakref.ref(a)
print(wr())
del a
print(wr())

# Test weakref.ref() with a weak reference to a cyclic reference.
class B:
    pass
b = B()
b.b = b
wr = weakref.ref(b)
print(wr())
del b
print(wr())

# Test weakref.ref() with a weak reference to a cyclic reference.
# (This time, the weak reference is in the cycle.)
class C:
    pass
c = C()
c.c = weakref.ref(c)
print(c.c())
del c
print(c.c())

# Test weakref.ref() with a weak reference to a cyclic reference.
# (This time, the weak reference is in the cycle, and the cycle
# is in a class.)
class D:
    def __init__(self):
        self.d = weakref.ref(self)
d = D()
