import weakref
# Test weakref.ref(self)
class C(object):
    def __init__(self, x):
        self.x = x
