import weakref
# Test weakref.ref() with a class instance

class C:
    def __init__(self):
        self.num = 0

def f():
    c = C()
    c.num = c.num + 1
    return c

def g():
    c = C()
    c.num = c.num + 1
    c2 = c
    return c2

def h():
    c = C()
    c.num = c.num + 1
    return c.num

def test_f():
    # f() returns a new instance each time
    i1 = weakref.ref(f())
    i2 = weakref.ref(f())
    assert i1() is not i2()

def test_g():
    # g() returns the same instance
    i1 = weakref.ref(g())
    i2 = weakref.ref(g())
    assert i1() is i2()

def test_h():
    # h() returns an int
    i1 = weakref.ref(h())
    i2 = weakref.ref(h())
