import weakref
# Test weakref.ref constructor for callability.

class C(object):
    def __call__(self):
        return True

class D(C):
    def __init__(self):
        self.value = 5

class E(D):
    pass

x = C()
y = D()
z = E()

# Check that all objects are callable
for o in [x,y,z]:
    print o()

# Check that all objects can be weakly referenced
for o in [x,y,z]:
    w = weakref.ref(o)
    print w()()

# Check that weakref of a subclass instance can still call the subclass's
# __call__() method.
w = weakref.ref(y)
print w()()

# Check that weakref of a subclass instance can still call the base class's
# __call__() method.
w = weakref.ref(z)
print w()()
