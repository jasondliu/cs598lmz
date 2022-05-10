fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_unhashable_cell
def f(x):
    return x

f.__code__.co_cellvars = (None,)

# test_code_unhashable_freevars
def f(x):
    return x

f.__code__.co_freevars = (None,)

# test_code_unhashable_names
def f(x):
    return x

f.__code__.co_names = (None,)

# test_code_unhashable_varnames
def f(x):
    return x

f.__code__.co_varnames = (None,)

# test_code_unhashable_cell2free
def f(x):
    return x

f.__code__.co_cellvars = ('y',)
f.__code__.co_freevars = ('y',)

# test_code_unhashable_free2cell
def f(x):
    return x

f.__code__.co
