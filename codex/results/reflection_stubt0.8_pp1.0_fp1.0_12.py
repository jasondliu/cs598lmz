fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code.co_code
fn()


def f():
    def g():
        def h():
            pass
        return h()

    return g()
f()


def f():
    class C:
        pass
    test_raises(TypeError, C, 12)
f()

def f():
    class C:
        pass
    test_raises(TypeError, int, 'qwert')
f()

def f():
    class C:
        def __init__(self, x):
            pass
    test_raises(TypeError, C, 12)
f()

def f():
    class C:
        def __init__(self, x):
            pass
    test_raises(TypeError, int, 'qwert')
f()

class A(object):
    pass

def f():
    class C(A):
        pass
    C()
f()

def f():
    class C(A):
        def __init__(self, x):
            pass
    C(12
