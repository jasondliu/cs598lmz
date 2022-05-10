fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

def f(x):
    if False:
        yield x

def g(x):
    if False:
        yield x
    else:
        yield x

def h(x):
    if False:
        yield x
    elif False:
        yield x
    else:
        yield x

class C:
    def __init__(self):
        if False:
            yield 1

g(0)
f(1)
h(2)

def f():
    if False:
        return
    yield 1

def f():
    if False:
        return
    yield 1
    if False:
        return
    yield 2

def f():
    if False:
        return
    yield 1
    if False:
        return
    yield 2
    if False:
        return
    yield 3

def f():
    if False:
        return
    yield 1
    if False:
        return
    yield 2
    if False:
        return
    yield 3
    if False:
