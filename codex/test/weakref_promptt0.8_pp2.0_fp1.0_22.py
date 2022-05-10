import weakref
# Test weakref.ref()

class C(object):
    def __init__(self, a):
        self.a = a
    def g(self):
        return str(self.a)

z = C(2)
x = weakref.ref(z)
y = weakref.ref(z)
