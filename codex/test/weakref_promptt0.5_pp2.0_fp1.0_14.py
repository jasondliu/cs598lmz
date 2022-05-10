import weakref
# Test weakref.ref()

class C(object):
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return 'C(%r)' % self.a

