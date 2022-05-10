fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# with a generator function
def g():
    yield

def fn():
    g()

gi = (i for i in ())
g.__code__ = gi
fn()

# with a generator function that raises StopIteration
def g():
    yield

def fn():
    g()

gi = (i for i in ())
next(gi)
g.__code__ = gi
fn()

# with a generator function that raises StopIteration
def g():
    yield

def fn():
    g()

gi = (i for i in ())
next(gi)
g.__code__ = gi
fn()

# with a generator function that raises StopIteration
def g():
    yield

def fn():
    g()

gi = (i for i in ())
next(gi)
g.__code__ = gi
fn()

# with a generator function that raises StopIteration
def g():
    yield

def fn():
    g()

gi = (i for i in ())
next
