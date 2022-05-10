fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 0
# Test fn.__code__.co_argcount for a function with a *args arg
def fn(*args):
    return args
fn.__code__.co_argcount = 4
# Test fn.__code__.co_argcount for a function with a *args arg and kwargs
def fn(*args, **kwargs):
    return args + tuple(kwargs.items())
fn.__code__.co_argcount = 8
# Test fn.__code__.co_argcount for a function with a kwsarg
def fn(**kwargs):
    return kwargs
fn.__code__.co_argcount = 8
# Test fn.__code__.co_argcount for a generator function
def fn():
    yield 42
fn.__code__.co_argcount = 2
# Test fn.__code__.co_argcount for a generator function with a default value
def fn(x=42):
    yield x
fn.__code__.co_argcount = 2

