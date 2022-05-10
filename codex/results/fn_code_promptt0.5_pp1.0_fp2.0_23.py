fn = lambda: None
# Test fn.__code__.co_argcount

assert fn.__code__.co_argcount == 0

def fn(x):
    pass

assert fn.__code__.co_argcount == 1

def fn(x, y):
    pass

assert fn.__code__.co_argcount == 2

def fn(x, y=1):
    pass

assert fn.__code__.co_argcount == 2

def fn(*args):
    pass

assert fn.__code__.co_argcount == 1

def fn(**kwargs):
    pass

assert fn.__code__.co_argcount == 1

def fn(x, *args):
    pass

assert fn.__code__.co_argcount == 2

def fn(x, **kwargs):
    pass

assert fn.__code__.co_argcount == 2

def fn(x, *args, **kwargs):
    pass

assert fn.__code__.co_argcount == 2

def fn(x, y=1, *args
