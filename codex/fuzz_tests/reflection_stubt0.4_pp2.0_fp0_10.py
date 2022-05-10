fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

#:
def fn():
    yield
fn()

#:
def fn():
    yield
    return
fn()

#:
def fn():
    return
    yield
fn()

#:
def fn():
    return
    yield
    return
fn()

#:
def fn():
    return
    yield
    return
    yield
fn()

#:
def fn():
    yield
    return
    yield
fn()

#:
def fn():
    yield
    return
    yield
    return
fn()

#:
def fn():
    yield
    return
    yield
    return
    yield
fn()

#:
def fn():
    return
    yield
    return
    yield
    return
fn()

#:
def fn():
    return
    yield
    return
    yield
    return
    yield
fn()

#:
def fn():
    return
    yield
    return
    yield
    return
    yield
    return
fn()

#
