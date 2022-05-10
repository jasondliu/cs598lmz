fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_argcount
fn.__code__.co_argcount

# Test fn.__code__.co_cellvars
def fn(a, b=10, c=20):
    def inner(x):
        nonlocal a
        nonlocal b
        nonlocal c
        return x + a + b + c
    return inner

fn(1).__code__.co_cellvars

# Test fn.__code__.co_code
fn.__code__.co_code

# Test fn.__code__.co_consts
fn.__code__.co_consts

# Test fn.__code__.co_filename
fn.__code__.co_filename

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno

# Test fn.__code__.co_flags
fn.__code__.co_flags

# Test fn.__code__.co_freevars
def fn(x, y):

