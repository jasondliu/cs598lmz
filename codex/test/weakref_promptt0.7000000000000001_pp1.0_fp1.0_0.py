import weakref
# Test weakref.ref for int and float
class X(object):
    def __init__(self, a):
        self.a = a
    def __hash__(self):
        return hash(self.a)
    def __repr__(self):
        return "X(%r)" % (self.a,)

x = X(1)
y = X(2)
wr = weakref.ref(x)
