import weakref
# Test weakref.ref() with a callable that raises an exception.
# This should not cause a segfault.

class C:
    def __init__(self):
        self.x = 1
    def f(self):
        raise Exception

def g(r):
    r()

c = C()
r = weakref.ref(c.f)
try:
    g(r)
except Exception:
    pass
