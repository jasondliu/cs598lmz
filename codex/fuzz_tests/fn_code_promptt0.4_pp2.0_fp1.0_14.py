fn = lambda: None
# Test fn.__code__.co_firstlineno
def f():
    pass
fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_lnotab
def f():
    pass
fn.__code__.co_lnotab = b''
# Test fn.__code__.co_consts
def f():
    pass
fn.__code__.co_consts = (1, None)
# Test fn.__code__.co_names
def f():
    pass
fn.__code__.co_names = ('a',)
# Test fn.__code__.co_varnames
def f():
    pass
fn.__code__.co_varnames = ('a',)
# Test fn.__code__.co_freevars
def f():
    pass
fn.__code__.co_freevars = ('a',)
# Test fn.__code__.co_cellvars
def f():
    pass
fn.__code__.co_cellvars = ('a',)
# Test fn.__code
