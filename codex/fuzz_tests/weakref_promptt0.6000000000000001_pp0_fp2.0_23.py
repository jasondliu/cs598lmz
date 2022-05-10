import weakref
# Test weakref.ref(int)
def f():
    return 42

class C:
    def __init__(self):
        self.x = 42

def g():
    return C()

for obj in (f, g):
    r = weakref.ref(obj)
    assert r() is obj
    assert r()() == 42
    assert r().x == 42

def f():
    pass

def g():
    pass

for obj in (f, g):
    r = weakref.ref(obj)
    assert r() is obj
    assert r() is None
