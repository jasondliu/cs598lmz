fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #1333
def f():
    def g():
        return 1
    return g

f()()

# Issue #1334
def f():
    def g():
        return 1
    return g

f()()

# Issue #1335
def f():
    def g():
        return 1
    return g

f()()

# Issue #1336
def f():
    def g():
        return 1
    return g

f()()

# Issue #1337
def f():
    def g():
        return 1
    return g

f()()

# Issue #1338
def f():
    def g():
        return 1
    return g

f()()

# Issue #1339
def f():
    def g():
        return 1
    return g

f()()

# Issue #1340
def f():
    def g():
        return 1
    return g

f()()

# Issue #1341
def f():
    def g():
       
