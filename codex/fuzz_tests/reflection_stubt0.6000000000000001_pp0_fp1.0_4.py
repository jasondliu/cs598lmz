fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
fn.__code__ = int
fn()


def f():
    yield 1


f.__code__ = 5
f()


def f():
    yield 1


c = f.__code__
c.__eq__ = lambda x: 1
f == f


class C:
    def f(self):
        yield 1


c = C()
c.f.__code__ = 5
c.f()


def f():
    yield 1


c = f.__code__
c.__eq__ = lambda x: 1
c == f


def f():
    yield 1


c = f.__code__
c.__eq__ = lambda x: 1
c == c


def f():
    yield 1


c = f.__code__
c.__eq__ = lambda x: 1
c == c


def f():
    yield 1


c = f.__code__
c.__eq__ = lambda x: 1
c == c


def f():
    yield 1


c = f.__
