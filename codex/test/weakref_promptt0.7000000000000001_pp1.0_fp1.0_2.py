import weakref
# Test weakref.ref subclasses

class A:
    pass

class ref(weakref.ref):
    def __init__(self, ob, callback=None):
        weakref.ref.__init__(self, ob, callback)
        self.invoked = 0
        self.args = None
    def __call__(self, *args):
        self.invoked = 1
        self.args = args
        return weakref.ref.__call__(self)

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

ra = ref(a)
rb = ref(b, ra)
rc = ref(c, rb)
rd = ref(d, rc)

del a, b, c, d

# Check that rd is dead
try:
    x = rd()
except ReferenceError:
    pass
