import weakref
# Test weakref.ref(lambda: None)

class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "A(%r)" % self.x

class B(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y

    def __repr__(self):
        return "B(%r, %r)" % (self.x, self.y)

class C(A):
    def __init__(self, x, y):
        A.__init__(self, x)
        self.y = y

    def __repr__(self):
        return "C(%r, %r)" % (self.x, self.y)

class D(B, C):
    def __init__(self, x, y, z):
        B.__init__(self, x, y)
        C.__init__(self, x, y)
        self.z = z

    def
