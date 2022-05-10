import gc, weakref

class Foo(object):
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return 'Foo(%s)' % self.val

