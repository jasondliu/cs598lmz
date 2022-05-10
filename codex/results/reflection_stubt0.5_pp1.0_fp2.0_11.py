fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #8136
def f():
    yield

class C:
    __code__ = f().gi_code

# Issue #8137
def f():
    class C:
        __code__ = f.__code__
f()

# Issue #8138
def f():
    class C:
        __code__ = f.__code__
f.__code__ = None
f()

# Issue #8139
def f():
    class C:
        __code__ = f.__code__
f.__code__ = f.__code__
f()

# Issue #8140
def f():
    class C:
        __code__ = f.__code__
f.__code__ = f.__code__
f()

# Issue #8141
def f():
    class C:
        __code__ = f.__code__
f.__code__ = f.__code__
f()

# Issue #8142
def f():
    class C:
        __code__ = f.__code
