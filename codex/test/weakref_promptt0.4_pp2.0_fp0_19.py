import weakref
# Test weakref.ref()
import gc

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return 'C(%r)' % self.x

# Create a reference cycle
a = C(C(C(C(5))))

# Create a weak reference to a
b = weakref.ref(a)

# Create a weak reference to a.x
c = weakref.ref(a.x)

# Create a weak reference to a.x.x
d = weakref.ref(a.x.x)

# Create a weak reference to a.x.x.x
e = weakref.ref(a.x.x.x)

# Create a weak reference to a.x.x.x.x
f = weakref.ref(a.x.x.x.x)

# Create a weak reference to a.x.x.x.x.x
g = weakref.ref(a.x.x.x.x.x)

# Create a weak reference to a.
