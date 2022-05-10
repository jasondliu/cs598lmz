fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #29275: segfault in _PyCode_GetExtra
def f():
    pass
f.__code__.co_extra = None
f()

# Issue #29276: segfault in _PyCode_GetExtra
def f():
    pass
f.__code__.co_extra = (1, 2, 3)
f()

# Issue #29277: segfault in _PyCode_GetExtra
def f():
    pass
f.__code__.co_extra = (1, 2, 3)
f.__code__.co_extra = None
f()

# Issue #29278: segfault in _PyCode_GetExtra
def f():
    pass
f.__code__.co_extra = (1, 2, 3)
f.__code__.co_extra = (1, 2, 3)
f()

# Issue #29279: segfault in _PyCode_GetExtra
def f():
    pass
f.__code__.co_extra = (
