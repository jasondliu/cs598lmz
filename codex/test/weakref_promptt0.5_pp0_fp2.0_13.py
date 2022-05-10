import weakref
# Test weakref.ref() with a callable object, and with a callable class instance.

class C:
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, *args):
        return self.arg

class D:
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, *args):
        return self.arg
    def __eq__(self, other):
        return self.arg == other.arg

class E(object):
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, *args):
        return self.arg

class F(object):
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, *args):
        return self.arg
    def __eq__(self, other):
        return self.arg == other.arg

def test_ref(c, t):
    r = weakref.ref(c)
    assert r() is c

