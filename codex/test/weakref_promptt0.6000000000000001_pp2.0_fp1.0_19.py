import weakref
# Test weakref.ref(f) with a callable object
class C(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args):
        return self.name, args

