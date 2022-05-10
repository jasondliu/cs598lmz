import weakref
# Test weakref.ref() with an object that implements the buffer protocol.

class A(object):
    def __init__(self, x):
        self.x = x
        self.b = buffer(x)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, i):
        return self.b[i]

    def __setitem__(self, i, y):
        self.b[i] = y


def callback(ref):
    print "callback", ref()

a = A([1, 2, 3])
r = weakref.ref(a, callback)
print "created", r
del a
print "deleted"
r()
