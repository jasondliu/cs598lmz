import weakref
# Test weakref.ref(x).__call__()

class Foo(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class Bar(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

