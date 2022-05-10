fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __code__.__annotations__
def fn():
    pass
fn.__code__.__annotations__ = {'a': 1}
fn.__annotations__

# Test __code__.co_consts
def fn():
    pass
fn.__code__.co_consts = (1, 2)
fn.__code__.co_consts

# Test __code__.co_varnames
def fn():
    pass
fn.__code__.co_varnames = ('a', 'b')
fn.__code__.co_varnames

# Test __code__.co_names
def fn():
    pass
fn.__code__.co_names = ('a', 'b')
fn.__code__.co_names

# Test __code__.co_freevars
def fn():
    pass
fn.__code__.co_freevars = ('a', 'b')
fn.__code__.co_freevars

# Test __code__.co_cellv
