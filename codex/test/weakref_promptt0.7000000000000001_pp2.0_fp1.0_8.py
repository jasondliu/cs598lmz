import weakref
# Test weakref.ref() for callable objects.

class C(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, x):
        return self.name + str(x)

c1 = C("c1")
c2 = C("c2")

r1 = weakref.ref(c1)
r2 = weakref.ref(c2)

eq(r1(1), "c11")
eq(r2(1), "c21")

# Test weakref.ref() on a callable object that overrides __del__.

class D(object):
    def __init__(self, name):
        self.name = name
        self.deleted = False
    def __call__(self, x):
        return self.name + str(x)
    def __del__(self):
        self.deleted = True

d1 = D("d1")
d2 = D("d2")

dr1 = weakref.ref(d1)
dr2 = weakref.ref
