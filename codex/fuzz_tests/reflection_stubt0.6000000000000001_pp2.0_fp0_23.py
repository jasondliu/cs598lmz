fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# ---

import dis

def fn():
    yield 1

dis.dis(fn)

# ---

import dis

def fn():
    for i in range(10):
        if i < 5:
            yield i

dis.dis(fn)

# ---

def fn():
    for i in range(10):
        if i < 5:
            yield i

g = fn()
g

# ---

def fn():
    for i in range(10):
        if i < 5:
            yield i

g = fn()
next(g)

# ---

def fn():
    for i in range(10):
        if i < 5:
            yield i

g = fn()
next(g)
next(g)

# ---

def fn():
    for i in range(10):
        if i < 5:
            yield i

g = fn()
list(g)

# ---

def fn():
    for i in range(10):
        if i
