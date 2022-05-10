fn = lambda: None
# Test fn.__code__.co_filename

class A:
    def f(self):
        pass
    def g(self):
        pass

def f():
    pass

def g():
    pass

def h():
    pass

class B:
    def __init__(self):
        self.f = f
        self.g = g
        self.h = h
        self.i = lambda: None

def test_function():
    assert f.__code__.co_filename == __file__
    assert g.__code__.co_filename == __file__
    assert h.__code__.co_filename == __file__
    assert fn.__code__.co_filename == __file__
    b = B()
    assert b.f.__code__.co_filename == __file__
    assert b.g.__code__.co_filename == __file__
    assert b.h.__code__.co_filename == __file__
    assert b.i.__code__.co_filename == __file__

class C:
    def f
