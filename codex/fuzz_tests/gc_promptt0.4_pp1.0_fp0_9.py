import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Create a cycle involving a class and an instance of that class
X = A()
X.foo = X
del X

# Create a cycle involving a class and an instance of a subclass
Y = B()
Y.foo = Y
del Y

# Create a cycle involving a class and an instance of a sibling class
Z = C()
Z.foo = Z
del Z

# Create a cycle involving a class and an instance of a subclass of a sibling class
T = D()
T.foo = T
del T

gc.collect()

# Create a cycle involving a dictionary and a function
def f():
    pass

d = {}
d[0] = f
f.foo = d
del f, d

gc.collect()

# Create a cycle involving a dictionary and a class
class E:
    pass

e = E()
d = {}
d[0] = e
e.
