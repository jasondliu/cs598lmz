import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a bunch of objects, then collect them.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

for i in range(10):
    A()
    B()
    C()
    D()
    E()

gc.collect()

# Create a cycle involving a dict.

d = {}
d[1] = d

# Create a cycle involving a list.

l = []
l.append(l)

# Create a cycle involving a custom object.

class F:
    pass

f = F()
f.v = f

# Create a cycle involving a custom object with a __del__ method.

class G:
    def __del__(self):
        pass

g = G()
g.v = g

# Create a cycle involving a custom object with a weakrefable instance
# variable.

class H:
    pass

class I:
    pass

