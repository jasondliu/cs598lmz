fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', lambda: None)
fn.__code__.co_varnames = (1, 2, 3)
fn.__code__.co_varnames = ()
fn.__code__.co_varnames = (1,)
fn.__code__.co_varnames = (1, 2)
fn.__code__.co_varnames = (1, 2, 3)

# Test fn.__code__.co_argcount
setattr(fn, '__code__', lambda: None)
fn.__code__.co_argcount = 0
fn.__code__.co_argcount = 1
fn.__code__.co_argcount = 2
fn.__code__.co_argcount = 3

# Test fn.__code__.co_cellvars
setattr(fn, '__code__', lambda: None)
fn.__code__.co_cellvars = (1, 2, 3)
fn.__code__.co_cellvars = ()

