fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn, gi

def f():
    yield

def g():
    yield
    return

def h():
    yield
    yield

def i():
    return

def j():
    raise StopIteration

def k():
    raise StopIteration
    yield

def l():
    raise StopIteration
    return

def m():
    raise StopIteration
    yield
    return

def n():
    try:
        yield
    except StopIteration:
        pass

def o():
    try:
        yield
    except StopIteration:
        pass
    return

def p():
    try:
        yield
    except StopIteration:
        pass
    yield

def q():
    try:
        yield
    except StopIteration:
        pass
    yield
    return

def r():
    try:
        yield
    except StopIteration:
        pass
    return
    yield

def s():
    try:
        yield
    except StopIteration:
        pass
    return
