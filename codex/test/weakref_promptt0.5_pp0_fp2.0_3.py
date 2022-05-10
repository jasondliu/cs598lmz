import weakref
# Test weakref.ref() with callable objects

class C:
    def __call__(self):
        return 42

def f():
    return 24

class E:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

def test_callable():
    c = C()
    r = weakref.ref(c)
    assert r()() == 42
    del c
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r()() == 42
    assert r
