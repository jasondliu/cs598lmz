fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# issue #7
def f():
    pass

f.__code__ = f.__code__

# issue #8
def f():
    pass

f.__code__ = f.__code__.__code__

# issue #9
def f():
    pass

f.__code__ = f.__code__.__code__.__code__

# issue #10
def f():
    pass

f.__code__ = f.__code__.__code__.__code__.__code__

# issue #11
def f():
    pass

f.__code__ = f.__code__.__code__.__code__.__code__.__code__

# issue #12
def f():
    pass

f.__code__ = f.__code__.__code__.__code__.__code__.__code__.__code__

# issue #13
def f():
    pass

f.__code__ = f.__code__.__code__.__code__
