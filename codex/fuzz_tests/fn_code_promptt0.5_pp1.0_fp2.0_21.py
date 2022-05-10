fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('a', 'b', 'c')
fn.__code__.co_varnames[0]
fn.__code__.co_varnames[1]
fn.__code__.co_varnames[2]
