import weakref
# Test weakref.ref(self) for callable objects

class C(object):
    def __init__(self, val):
        self.val = val
    def __call__(self):
        return self.val
    def __hash__(self):
        return hash(self.val)

