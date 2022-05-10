fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #24
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #25
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #26
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #27
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #28
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #29
def f():
    pass

def g():
    pass

f.__code__ = g.__code__
f()

# issue #30
def f():
    pass

def g():
    pass

f.__code__
