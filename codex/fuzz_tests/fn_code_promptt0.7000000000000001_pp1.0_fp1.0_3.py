fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()
fn.__code__.co_varnames = (1, 2, 3)
fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__code__.co_names
fn.__code__.co_names = ()
fn.__code__.co_names = (1, 2, 3)
fn.__code__.co_names = ('a', 'b', 'c')

# Test fn.__code__.co_argcount
fn.__code__.co_argcount = 0
fn.__code__.co_argcount = 1
fn.__code__.co_argcount = 2
fn.__code__.co_argcount = 3

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 0
fn.__code__.co_firstlineno = 1
fn.__code__.co_firstlineno = 2

# Test fn.__
