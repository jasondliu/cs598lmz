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

gc.collect()
gc.collect()
gc.collect()

# Create a reference cycle
l1 = []
l2 = [l1]
l1.append(l2)

del l1, l2

gc.collect()
gc.collect()
gc.collect()

# Create a reference cycle involving instances
class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name

a = A('a')
b = A('b')
a.other = b
b.other = a

del a, b

gc.collect()
gc.collect()
gc.collect()

# Create a reference cycle involving instances and classes
class A:
    def __init__(self, name):
        self.name = name
    def __repr__(self
