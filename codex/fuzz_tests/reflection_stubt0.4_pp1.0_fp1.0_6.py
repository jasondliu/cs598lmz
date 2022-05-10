fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #1175
def f():
    yield 1

def g():
    yield 1

f.__code__ = g.__code__

# Issue #1176
def f():
    yield 1

def g():
    yield 1

f.__code__ = g.__code__
f()

# Issue #1177
def f():
    yield 1

def g():
    yield 1

f.__code__ = g.__code__
f.__code__ = f.__code__

# Issue #1178
def f():
    yield 1

def g():
    yield 1

f.__code__ = g.__code__
f.__code__ = f.__code__
f()

# Issue #1179
def f():
    yield 1

def g():
    yield 1

f.__code__ = g.__code__
f.__code__ = f.__code__
f.__code__ = f.__code__

# Issue #1180
def f():
