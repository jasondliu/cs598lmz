fn = lambda: None
# Test fn.__code__.co_firstlineno

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_firstlineno

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_firstlineno

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_firstlineno

# Test fn.__code__.co_flags

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_flags

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_flags

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_flags

# Test fn.__code__.co_lnotab

def f():
    pass
fn.__code__ = f.__code__
fn.__code__.co_lnotab

def
