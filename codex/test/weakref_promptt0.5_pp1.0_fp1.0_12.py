import weakref
# Test weakref.ref
class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "<C %s>" % self.x

c = C(1)
r = weakref.ref(c)
