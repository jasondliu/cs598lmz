import weakref
# Test weakref.ref() with new-style objects

class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

a = A()
b = B()
c = C()
d = D()

# Reference cycle
# a -> b -> c -> a
a.b = b
b.c = c
c.a = a

# Reference cycle
# a -> b -> c -> d -> a
a.b = b
b.c = c
c.d = d
d.a = a

# Reference cycle
# a -> b -> c -> d -> a
a.b = b
b.c = c
c.d = d
d.a = a

# Reference cycle
# a -> b -> c -> d -> b
a.b = b
b.c = c
c.d = d
d.b = b

del a, b, c, d

try:
    weakref.ref(A())
except TypeError:
    pass
else:
   
