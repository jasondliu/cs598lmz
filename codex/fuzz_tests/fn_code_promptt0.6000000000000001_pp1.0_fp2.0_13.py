fn = lambda: None
# Test fn.__code__.co_argcount

def foo(x, y): pass
fn.__code__ = foo.__code__
fn.__code__.co_argcount

def foo(): pass
fn.__code__ = foo.__code__
fn.__code__.co_argcount

def foo(*args): pass
fn.__code__ = foo.__code__
fn.__code__.co_argcount

def foo(**kwargs): pass
fn.__code__ = foo.__code__
fn.__code__.co_argcount

def foo(*args, **kwargs): pass
fn.__code__ = foo.__code__
fn.__code__.co_argcount

# Test fn.__code__.co_consts

def foo(x, y): pass
fn.__code__ = foo.__code__
fn.__code__.co_consts

def foo(): pass
fn.__code__ = foo.__code__
fn.__code__.co_consts

def foo():
    return 1
fn.__
