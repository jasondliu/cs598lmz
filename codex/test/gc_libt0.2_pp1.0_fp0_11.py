import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'A(%s)' % self.name
