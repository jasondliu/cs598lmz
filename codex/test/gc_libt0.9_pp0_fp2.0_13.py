import gc, weakref

class A:

    def __init__(self, val=99):
        print('init', self)
        self.val = val

    def __repr__(self):
        return 'A(%s)' % self.val


