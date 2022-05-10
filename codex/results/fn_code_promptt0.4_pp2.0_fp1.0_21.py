fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount

# Test fn.__code__.co_cellvars
def fn(a, b):
    c = 1
    d = 2
    def inner():
        nonlocal c
        c += 1
fn.__code__.co_cellvars

# Test fn.__code__.co_consts
fn.__code__.co_consts

# Test fn.__code__.co_filename
fn.__code__.co_filename

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno

# Test fn.__code__.co_flags
fn.__code__.co_flags

# Test fn.__code__.co_freevars
fn.__code__.co_freevars

# Test fn.__code__.co_kwonlyargcount
fn.__code__.co_kwonlyargcount

# Test fn.__code__.co_lnotab
fn.__code__.co_l
