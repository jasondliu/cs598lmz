fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()


class C:
    def x(self):
        pass


def f():
    pass


def g():
    pass


def h():
    pass


C.x.__code__ = f.__code__
f.__code__ = g.__code__
g.__code__ = h.__code__
C.x()
f()
g()
h()

C.y = 3
delattr(C, "y")
