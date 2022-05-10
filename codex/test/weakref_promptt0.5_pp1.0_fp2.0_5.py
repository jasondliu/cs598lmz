import weakref
# Test weakref.ref() on a callable object.
class C(object):
    def __init__(self, n):
        self.n = n

    def __call__(self):
        return self.n

def f(x):
    return x + 1

def g():
    return 42

for x in [C(1), f, g, (lambda: None)]:
    r = weakref.ref(x)
    assert r() is x
    assert r()() == x()

try:
    import thread
except ImportError:
    pass
else:
    # Test weakref.ref() on a lock object.
    lock = thread.allocate_lock()
    r = weakref.ref(lock)
    assert r() is lock
    assert r() is lock
    del lock
    assert r() is None

# Test weakref.proxy() on a callable object.
class C(object):
    def __init__(self, n):
        self.n = n

    def __call__(self):
        return self.n

