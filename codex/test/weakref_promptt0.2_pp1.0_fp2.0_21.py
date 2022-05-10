import weakref
# Test weakref.ref() with a class that has a __del__ method.
# This is a regression test for SF bug #813900.

class C:
    def __init__(self, arg):
        self.arg = arg
    def __del__(self):
        pass

def f():
    c = C(1)
    r = weakref.ref(c)
    return r

r = f()
