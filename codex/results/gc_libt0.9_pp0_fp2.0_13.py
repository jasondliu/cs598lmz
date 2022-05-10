import gc, weakref

class A:

    def __init__(self, val=99):
        print('init', self)
        self.val = val

    def __repr__(self):
        return 'A(%s)' % self.val


a1 = A(1)
print(dir(a1))

print(dir(a1.__class__))

print(dir(gc))
