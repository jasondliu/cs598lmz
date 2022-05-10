fn = lambda: None
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 1

def fn(a):
    pass
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 1

def fn(*a):
    pass
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 0

def fn(**a):
    pass
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 0

def fn(*a, **b):
    pass
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 0

def fn(a, *b, **c):
    pass
# Test fn.__code__.co_argcount.
fn.__code__.co_argcount  # 1

# Test fn.__code__.co_varnames.
fn.__code__.co_varnames  # ('a', 'b
