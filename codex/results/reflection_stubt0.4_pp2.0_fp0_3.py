fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def f():
    print('f')
    yield 1

f().send(None)


def f():
    print('f')
    yield 1

f().__next__()


def f():
    print('f')
    yield 1

g = f()
g.send(None)


def f():
    print('f')
    yield 1

g = f()
g.__next__()


def f():
    print('f')
    yield 1

g = f()
next(g)


def f():
    print('f')
    yield 1

g = f()
iter(g)


def f():
    print('f')
    yield 1

g = f()
g.__iter__()


def f():
    print('f')
    yield 1

g = f()
g.__next__()


def f():
    print('f')
    yield 1

g = f()
g.send(None)


def f():
    print('f')

