import weakref
# Test weakref.ref() and weakref.proxy() with a class instance.

class C(object):
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return 'C(%s)' % self.n

