import weakref
# Test weakref.ref to a class instance

class A:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return "A(%s)" % self.val

a = A(10)
r = weakref.ref(a)
