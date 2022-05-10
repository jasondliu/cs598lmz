fn = lambda: None
# Test fn.__code__.co_consts
fn.__code__.co_consts = (1, None, 'x')

# Test fn.__code__.co_varnames
fn.__code__.co_varnames = tuple(map(chr, range(97, 123)))

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 5
