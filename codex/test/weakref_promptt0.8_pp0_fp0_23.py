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
