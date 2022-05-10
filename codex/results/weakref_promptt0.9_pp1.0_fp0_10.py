import weakref
# Test weakref.ref() being garbage collected.

class A:
    pass


class B:
    pass
a = A()

# Not collected.
wr = weakref.ref(a)
wr() is a

# Collected with finalizer.
def f(r):
    print "collected"
wr = weakref.ref(a, f)
del a


# Implements the 
class C(object):
    # For simplicity.
    keep_alive = []
    __slots__ = ['inst', 'ref', 'ref2', 'slots']

    def __init__(self):
        self.keep_alive = [self]
        self.inst = A()
        self.ref = weakref.ref(self.inst)
        self.slots = weakref.ref(self, self.callback)

    def gc(self):
        return self.ref() is None and self.ref2() is None

    def callback(self, ref):
        self.ref2 = weakref.ref(A(), self.callback_check)

    def callback_check
