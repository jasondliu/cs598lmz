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

# Create a cycle involving a class

X = A()
X.foo = X
del X
gc.collect()

# Create a cycle involving a dict

d = {}
d[1] = d
del d
gc.collect()

# Create a cycle involving a list

l = []
l.append(l)
del l
gc.collect()

# Create a cycle involving a tuple

t = (1, 2, 3)
t = t + (t,)
del t
gc.collect()

# Create a cycle involving a builtin function

def f():
    pass

f.foo = f
del f
gc.collect()

# Create a cycle involving a builtin method

class E:
    def foo(self):
        pass

x = E()
x.foo = x.foo
del x
gc.collect()

# Create a cycle involving a user
